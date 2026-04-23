'''
Anotações:
Rotas de usuário
raise --> fazer um erro de proposito e parar a função na hora
if not é 'se nao for'
HTTPException devolve um erro organizado pro app quando algo dá errado.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from service.database import get_db
from model.models import Usuario
from schemas.user import UsuarioResponse
from config.security import hash_senha, verificar_senha

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/register', response_model=UsuarioResponse)
def register(nome: str, email: str, senha: str, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    criptografada = hash_senha(senha)
    
    novo_usuario = Usuario(nome=nome, email=email, senha=criptografada)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


@auth_router.post('/login')
def login(email: str, senha: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    if not verificar_senha(senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Senha incorreta")
    
    return {"message": "Login realizado com sucesso!"}

@auth_router.put('/alterar-senha')
def alterar_senha(
    email: str,
    senha_atual: str,
    nova_senha: str,
    db: Session = Depends(get_db)
):
    # busca o usuario pelo email
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # verifica se a senha atual está correta
    if not verificar_senha(senha_atual, usuario.senha):
        raise HTTPException(status_code=401, detail="Senha atual incorreta")

    # criptografa a nova senha e salva
    usuario.senha = hash_senha(nova_senha)
    db.commit()

    return {"message": "Senha alterada com sucesso!"}

@auth_router.post('/logout')
def logout():
    # o front é responsável por apagar o token
    # essa rota só confirma que o logout foi solicitado
    return {"message": "Logout realizado com sucesso!"}