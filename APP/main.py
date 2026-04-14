#NOTE - para rodar o código: uvicorn APP.main:app --reload

from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from api.V1.endpoints import auth
from api.V1.endpoints import consumo
from api.V1.endpoints import meta
from api.V1.endpoints import dica
from api.V1.router import usuario_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield # --> segurança de festa, deixa que eu(Infantini) explico

app = FastAPI(
    title="API de Monitoramento de Consumo Sustentável",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
def health_check():
    return {"status": "API no ar!"}

app.include_router(auth.auth_router)
app.include_router(consumo.consumo_router)
app.include_router(meta.meta_router)
app.include_router(dica.dica_router)
app.include_router(usuario_router)