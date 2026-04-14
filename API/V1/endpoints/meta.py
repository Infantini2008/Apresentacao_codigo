from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from SCHEMAS.meta import MetaCriar, MetaResponse
from MODELS.models import Meta, Consumo

meta_router = APIRouter(prefix="/metas", tags=["Metas"])

@meta_router.get("/")
def listar_metas(db: Session = Depends(get_db)):
    return db.query(Meta).all()

@meta_router.get("/usuario/{id_usuario}")
def metas_por_usuario(id_usuario: int, db: Session = Depends(get_db)):
    return db.query(Meta).filter(Meta.id_usuario == id_usuario).all()

@meta_router.post("/", response_model=MetaResponse)
def criar_meta(meta: MetaCriar, id_usuario: int, db: Session = Depends(get_db)):
    nova_meta = Meta(
        id_usuario=id_usuario,
        tipo_consumo=meta.tipo_consumo,
        valor_meta=meta.valor_meta,
        periodo=meta.periodo
    )
    db.add(nova_meta)
    db.commit()
    db.refresh(nova_meta)
    return nova_meta

@meta_router.put("/{id}", response_model=MetaResponse)
def editar_meta(id: int, meta: MetaCriar, db: Session = Depends(get_db)):
    meta_existente = db.query(Meta).filter(Meta.id == id).first()
    if not meta_existente:
        raise HTTPException(status_code=404, detail="Meta não encontrada")
    meta_existente.tipo_consumo = meta.tipo_consumo
    meta_existente.valor_meta = meta.valor_meta
    meta_existente.periodo = meta.periodo
    db.commit()
    db.refresh(meta_existente)
    return meta_existente

@meta_router.delete("/{id}")
def deletar_meta(id: int, db: Session = Depends(get_db)):
    meta = db.query(Meta).filter(Meta.id == id).first()
    if not meta:
        raise HTTPException(status_code=404, detail="Meta não encontrada")
    db.delete(meta)
    db.commit()
    return {"message": "Meta deletada com sucesso"}

@meta_router.get("/{id}/progresso")
def progresso_meta(id: int, db: Session = Depends(get_db)):
    meta = db.query(Meta).filter(Meta.id == id).first()
    if not meta:
        raise HTTPException(status_code=404, detail="Meta não encontrada")
    if meta.valor_meta == 0:
        raise HTTPException(status_code=400, detail="Valor da meta não pode ser zero")

    consumos = db.query(Consumo).filter(
        Consumo.id_usuario == meta.id_usuario,
        Consumo.tipo_consumo == meta.tipo_consumo
    ).all()

    total_consumido = sum(c.valor for c in consumos)

    percentual = (total_consumido / float(meta.valor_meta)) * 100
    diferenca = float(meta.valor_meta) - total_consumido

    return {
        "meta": float(meta.valor_meta),
        "consumido": total_consumido,
        "percentual": round(percentual, 2),
        "diferenca": round(diferenca, 2)
    }