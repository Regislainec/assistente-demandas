from pydantic import BaseModel
from typing import Optional

class Demanda(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    status: str
    nome_responsavel: str
    email_responsavel: str
    solicitante: str
    delegado: str
    prazo_entrega: str
    prazo_estimado: Optional[str] = None
    data_conclusao: Optional[str] = None
    reajuste_necessario: Optional[bool] = False
    justificativa_reajuste: Optional[str] = None
