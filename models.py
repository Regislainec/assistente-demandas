from pydantic import BaseModel
from typing import Literal
from datetime import date

class Demanda (BaseModel):
    titulo: str
    descricao: str
    nome_responsavel: str
    email_responsavel: str
    prioridade: Literal["Alta", "Média", "Baixa"]
    prazo_entrega: date
    status: Literal["Aberta", "Em Andamento", "Concluída"]
