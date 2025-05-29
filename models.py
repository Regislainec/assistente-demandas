from pydantic import BaseModel, EmailStr
from datetime import date

class Demanda(BaseModel):
    titulo: str
    descricao: str
    nome_responsavel: str
    email_responsavel: str
    prioridade: str
    prazo_entrega: date
    status: str
