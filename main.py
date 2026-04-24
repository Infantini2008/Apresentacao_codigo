
'''
ARQUIVO: main.py
FUNÇÃO: Ponto de entrada da API. Liga tudo — registra as rotas,
        configura o banco e sobe o servidor.
RODAR: uvicorn main:app --reload
'''


from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import Response
from service.database import create_tables
from routes.V1.endpoints import auth
from routes.V1.endpoints import consumo
from routes.V1.endpoints import meta
from routes.V1.endpoints import dica
from routes.V1.router import usuario_router
import json


def uppercase_values(data):
    '''
    Função recursiva que percorre todo o JSON da resposta
    e converte cada texto para letras maiúsculas.
    Números, booleanos e nulos não são alterados.
    '''
    if isinstance(data, dict):
        return {k: uppercase_values(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [uppercase_values(i) for i in data]
    elif isinstance(data, str):
        return data.upper()
    return data


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="API de Monitoramento",
    version="1.0.0",
    lifespan=lifespan
)


@app.middleware("http")
async def uppercase_middleware(request: Request, call_next):
    '''
    Middleware que intercepta todas as respostas da API
    e converte os textos para maiúsculas antes de enviar pro app.
    Middleware = código que roda em TODA requisição automaticamente.
    '''
    response = await call_next(request)

    body = b""
    async for chunk in response.body_iterator:
        body += chunk

    try:
        data = json.loads(body)
        body = json.dumps(uppercase_values(data)).encode()
    except:
        pass

    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )


@app.get("/")
def health_check():
    return {"status": "API no ar!"}


app.include_router(auth.auth_router)
app.include_router(consumo.consumo_router)
app.include_router(meta.meta_router)
app.include_router(dica.dica_router)
app.include_router(usuario_router)