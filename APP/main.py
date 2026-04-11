#NOTE -  Ponto de entrada da aplicação
#para rodar o código, usar: ''uvicorn main:app --reload'' no terminal

from fastapi import FastAPI

app = FastAPI()

from api.V1.endpoints import auth
from api.V1.endpoints import tracker

app.include_router(auth.auth_router)
app.include_router(tracker.tracker_router)