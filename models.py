from pydantic import BaseModel, EmailStr
from typing import Literal
from datetime import date

class DemandCreate(BaseModel):
    titulo: str
    descricao: str
    nome_responsavel: str
    email_responsavel: str
    prioridade: Literal["Alta", "Média", "Baixa"]
    prazo_entrega: date
    status: Literal["Aberta", "Em Andamento", "Concluída"]
