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