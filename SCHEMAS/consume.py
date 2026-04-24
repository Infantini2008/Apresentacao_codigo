'''
ARQUIVO: schemas/consume.py
FUNÇÃO: Define o formato dos dados que entram e saem da API.
        Classes que terminam em "Criar" = dados que o app manda.
        Classes que terminam em "Response" = dados que a API devolve.
        O Pydantic valida automaticamente se os dados estão corretos.
'''

from pydantic import BaseModel
from datetime import datetime

class ConsumoCriar(BaseModel):
    tipo_consumo: str
    valor: float
    unidade_medida: str
    data_registro: datetime = None
    is_simulado: bool = False

class ConsumoResponse(BaseModel):
    id: int
    id_usuario: int
    tipo_consumo: str
    valor: float
    unidade_medida: str
    data_registro: datetime
    is_simulado: bool

    class Config:
        from_attributes = True
