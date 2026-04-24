#NOTE -  Modelos do Banco (tabelas)

'''
ARQUIVO: models.py
FUNÇÃO: Define as tabelas do banco de dados como classes Python.
        Cada classe = uma tabela. Cada atributo = uma coluna.
        SQLAlchemy traduz as classes para SQL automaticamente.
'''

#importações
from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, ForeignKey, Boolean
from sqlalchemy.sql import func

#cria a base do banco
from service.base import Base

#criar classes e tabelas do banco
class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    senha = Column(String(255), nullable=False)
    email = Column(String(50), nullable=False, unique=True)


class Consumo(Base):
    __tablename__ = "consumo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False)
    tipo_consumo = Column(String(120), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    unidade_medida = Column(String(120), nullable=False)
    data_registro = Column(DateTime(timezone=True), server_default=func.now())
    is_simulado = Column(Boolean, default=False)   


class Meta(Base):
    __tablename__ = "meta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False)
    tipo_consumo = Column(String(80), nullable=False)
    valor_meta = Column(Numeric(10, 2), nullable=False)
    periodo = Column(String(20), nullable=False)


class Dicas(Base):
    __tablename__ = "dicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_consumo = Column(String(100))
    descricao = Column(Text, nullable=False)