from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

from models import DemandCreate
from database import create_demand, get_all_demands
from email_utils import enviar_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/demanda")
def criar_demanda(demanda: DemandCreate):
    try:
        create_demand(demanda)
        # Alerta de prazo para o responsável
        if demanda.email_responsavel:
            assunto = "Nova demanda atribuída"
            mensagem = f"""
            Você recebeu uma nova demanda:
            - Título: {demanda.titulo}
            - Descrição: {demanda.descricao}
            - Prazo para entrega: {demanda.prazo_entrega.strftime('%d/%m/%Y')}
            """
            enviar_email(demanda.email_responsavel, assunto, mensagem)
        return {"mensagem": "Demanda criada com sucesso!"}
    except Exception as e:
        return {"erro": f"Erro ao criar demanda: {str(e)}"}

@app.get("/demandas")
def listar_demandas():
    return get_all_demands()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # ← Corrigido aqui!
    uvicorn.run(app, host="0.0.0.0", port=port)
