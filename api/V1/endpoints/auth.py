#NOTE -  Rotas de usuário
from fastapi import APIRouter
from MODELS.models import user

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/user')
async def home(): 
    return {'mensage': 'you opened the route user'}

@auth_router.post('/create_user')
async def create_user(nome: str, email: str, senha: str):
    pass