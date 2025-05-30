from datetime import datetime, timedelta
from database import get_all_demanda
from email_utils import enviar_email
from fastapi import FastAPI

app = FastAPI()

def verificar_prazos():
    hoje = datetime.now().date()
    demandas = get_all_demanda()
    for demanda in demandas:
        prazo = datetime.strptime(demanda["prazo_entrega"], "%Y-%m-%d").date()
        if prazo - hoje == timedelta(days=1):
            assunto = "⚠️ Prazo de demanda se encerrando"
            corpo = f"A demanda '{demanda['titulo']}' está com prazo de entrega para amanhã.\nResponsável: {demanda['responsavel']}"
            enviar_email(demanda["email_responsavel"], assunto, corpo)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
