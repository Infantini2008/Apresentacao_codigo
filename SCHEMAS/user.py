#NOTE -  Schemas Pydantic (validação/serialização)

'''
ARQUIVO: schemas/user.py
FUNÇÃO: Define o formato dos dados que entram e saem da API.
        Classes que terminam em "Criar" = dados que o app manda.
        Classes que terminam em "Response" = dados que a API devolve.
        O Pydantic valida automaticamente se os dados estão corretos.
'''

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