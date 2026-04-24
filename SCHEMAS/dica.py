'''
ARQUIVO: schemas/dica.py
FUNÇÃO: Define o formato dos dados que entram e saem da API.
        Classes que terminam em "Criar" = dados que o app manda.
        Classes que terminam em "Response" = dados que a API devolve.
        O Pydantic valida automaticamente se os dados estão corretos.
'''

from pydantic import BaseModel

class DicaCriar(BaseModel):
    tipo_consumo: str
    descricao: str

class DicaResponse(BaseModel):
    id: int
    tipo_consumo: str
    descricao: str

    class Config:
        from_attributes = True