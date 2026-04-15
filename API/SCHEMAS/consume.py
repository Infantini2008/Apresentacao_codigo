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
