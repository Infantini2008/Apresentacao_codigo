'''
ARQUIVO: schemas/meta.py
FUNÇÃO: Define o formato dos dados que entram e saem da API.
        Classes que terminam em "Criar" = dados que o app manda.
        Classes que terminam em "Response" = dados que a API devolve.
        O Pydantic valida automaticamente se os dados estão corretos.
'''

from pydantic import BaseModel

class MetaCriar(BaseModel):
    tipo_consumo: str
    valor_meta: float
    periodo: str

class MetaResponse(BaseModel):
    id: int
    id_usuario: int
    tipo_consumo: str
    valor_meta: float
    periodo: str

    class Config:
        from_attributes = True