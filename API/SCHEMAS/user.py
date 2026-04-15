#NOTE -  Schemas Pydantic (validação/serialização)
from pydantic import BaseModel

'''
base model é uma classe base do pydantic

usuarioresponse define o que vai aparecer na resposta (não mostrar a senha)

from_atributes fala que não vem de um dicionario e sim um banco
'''

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True