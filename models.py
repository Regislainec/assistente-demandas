from pydantic import BaseModel, EmailStr
from datetime import date

class DemandCreate(BaseModel):
    titulo: str
    descricao: str
    responsavel: str
    email_responsavel: EmailStr
    prazo_entrega: date
