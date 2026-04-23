#NOTE - para rodar o código: uvicorn main:app --reload

from contextlib import asynccontextmanager
from fastapi import FastAPI
from service.database import create_tables
from routes.V1.endpoints import auth
from routes.V1.endpoints import consumo
from routes.V1.endpoints import meta
from routes.V1.endpoints import dica
from routes.V1.router import usuario_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    title="API de Monitoramento",
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