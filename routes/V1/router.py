from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from service.database import get_db
from model.models import Usuario

usuario_router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@usuario_router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@usuario_router.get("/{id}")
def buscar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@usuario_router.delete("/{id}")
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"message": "Usuário deletado com sucesso"}