from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from service.database import get_db
from model.models import Consumo
#para o consumo saber o formato dos dados que vão entrar e sair da rota.
from schemas.consume import ConsumoCriar, ConsumoResponse

consumo_router = APIRouter(prefix="/consumos", tags=["Consumos"])

@consumo_router.get("/")
def listar_consumos(db: Session = Depends(get_db)):
    return db.query(Consumo).all()

@consumo_router.get("/usuario/{id_usuario}")
def consumos_por_usuario(id_usuario: int, db: Session = Depends(get_db)):
    return db.query(Consumo).filter(Consumo.id_usuario == id_usuario).all()

@consumo_router.post("/", response_model=ConsumoResponse)
def criar_consumo(consumo: ConsumoCriar, id_usuario: int, db: Session = Depends(get_db)):
    novo_consumo = Consumo(
        id_usuario=id_usuario,
        tipo_consumo=consumo.tipo_consumo,
        valor=consumo.valor,
        unidade_medida=consumo.unidade_medida,
        is_simulado=consumo.is_simulado
    )
    db.add(novo_consumo)
    db.commit()
    db.refresh(novo_consumo)
    return novo_consumo

@consumo_router.delete("/{id}")
def deletar_consumo(id: int, db: Session = Depends(get_db)):
    consumo = db.query(Consumo).filter(Consumo.id == id).first()
    if not consumo:
        raise HTTPException(status_code=404, detail="Consumo não encontrado")
    db.delete(consumo)
    db.commit()
    return {"message": "Consumo deletado com sucesso"}

@consumo_router.put("/{id}", response_model=ConsumoResponse)
def editar_consumo(id: int, consumo: ConsumoCriar, db: Session = Depends(get_db)):
    # busca o consumo pelo id
    consumo_existente = db.query(Consumo).filter(Consumo.id == id).first()
    if not consumo_existente:
        raise HTTPException(status_code=404, detail="Consumo não encontrado")

    # atualiza os campos com os novos valores
    consumo_existente.tipo_consumo = consumo.tipo_consumo
    consumo_existente.valor = consumo.valor
    consumo_existente.unidade_medida = consumo.unidade_medida
    consumo_existente.is_simulado = consumo.is_simulado

    db.commit()
    db.refresh(consumo_existente)
    return consumo_existente