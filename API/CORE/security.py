#NOTE -  JWT, hash de senha, etc.
import bcrypt

#TODO - hash é como se fosse uma digital

'''
crypt context vai criptografar algo
ex: temos uma senha --> 'KarythonMeDaPonto3000'
o crypt vai ver essa senha e falar: 'pô, até o infantini pode descobrir essa senha!' e vai tranformar a senha em algo tipo: 'sdkljgbasdklhjfsdnklçjfgsakçjgsadjkl'

-Davi Coelho pergunta:
    mas como o banco vai garantir que a senha está certa?

pra isso temos a def de verificar senha, ela basicamente vai pegar a senha que o usuario colocou e vai criptografar, se ficar igual, é a senha que o usuario colocou
'''

def hash_senha(senha: str) -> str:
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha_bytes, salt).decode('utf-8')

def verificar_senha(senha: str, senha_hash: str) -> bool:
    senha_bytes = senha.encode('utf-8')
    hash_bytes = senha_hash.encode('utf-8')
    return bcrypt.checkpw(senha_bytes, hash_bytes)