from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from MODELS.models import Dicas
from SCHEMAS.dica import DicaCriar, DicaResponse

dica_router = APIRouter(prefix="/dicas", tags=["Dicas"])

@dica_router.get("/")
def listar_dicas(db: Session = Depends(get_db)):
    return db.query(Dicas).all()

@dica_router.get("/tipo/{tipo_consumo}")
def dicas_por_tipo(tipo_consumo: str, db: Session = Depends(get_db)):
    return db.query(Dicas).filter(Dicas.tipo_consumo == tipo_consumo).all()

@dica_router.post("/", response_model=DicaResponse)
def criar_dica(dica: DicaCriar, db: Session = Depends(get_db)):
    nova_dica = Dicas(
        tipo_consumo=dica.tipo_consumo,
        descricao=dica.descricao
    )
    db.add(nova_dica)
    db.commit()
    db.refresh(nova_dica)
    return nova_dica

@dica_router.delete("/{id}")
def deletar_dica(id: int, db: Session = Depends(get_db)):
    dica = db.query(Dicas).filter(Dicas.id == id).first()
    if not dica:
        raise HTTPException(status_code=404, detail="Dica não encontrada")
    db.delete(dica)
    db.commit()
    return {"message": "Dica deletada com sucesso"}