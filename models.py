
from sqlalchemy import Column, Integer, String
from database import Base

class Demanda(Base):
    __tablename__ = "demandas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    email_responsavel = Column(String)
    status = Column(String, default="pendente")
    justificativa_correcao = Column(String, nullable=True)
    novo_prazo = Column(String, nullable=True)
