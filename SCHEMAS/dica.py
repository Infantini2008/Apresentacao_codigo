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