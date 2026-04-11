#NOTE -  Exemplo de outro recurso
from fastapi import APIRouter

tracker_router = APIRouter(prefix='/tracker', tags=['tracker'])

@tracker_router.get('/Mconsume')   
async def consume():
    return {'mensage': 'you opened the route consume'}