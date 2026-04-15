'''
Anotações:
Rotas de usuário
raise --> fazer um erro de proposito e parar a função na hora
if not é 'se nao for'
HTTPException devolve um erro organizado pro app quando algo dá errado.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from MODELS.models import Usuario
from SCHEMAS.user import UsuarioResponse
from CORE.security import hash_senha, verificar_senha

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/register', response_model=UsuarioResponse)
def register(nome: str, email: str, senha: str, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    '''
    a hash vai basicamente dar o tempero para que sua senha seja unica
    '''
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
    
    '''
    vê se tem o tempero 
    '''
    if not verificar_senha(senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Senha incorreta")
    
    return {"message": "Login realizado com sucesso!"}
