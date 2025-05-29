
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Demanda
from email_utils import enviar_email

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Assistente de Demandas - API Online"}
@app.put("/demandas/{demanda_id}/correcao")
def solicitar_correcao(demanda_id: int, justificativa: str, novo_prazo: str, db: Session = Depends(SessionLocal)):
    demanda = db.query(Demanda).filter(Demanda.id == demanda_id).first()
    if not demanda:
        raise HTTPException(status_code=404, detail="Demanda não encontrada")

    demanda.justificativa_correcao = justificativa
    demanda.novo_prazo = novo_prazo
    demanda.status = "correcao_pendente"
    db.commit()

    assunto = f"[Correção solicitada] Demanda: {demanda.titulo}"
    mensagem = f"""Olá,\n\nFoi solicitada uma correção na demanda:\n\nTítulo: {demanda.titulo}
Justificativa: {justificativa}
Novo prazo: {novo_prazo}\n\nPor favor, acesse o sistema e atualize a tarefa.

Att, Sistema de Demandas"""
    enviar_email(demanda.email_responsavel, assunto, mensagem)
    return {"message": "Correção registrada e e-mail enviado."}
if __name__ == "__main__":
    import uvicorn
 import os

port = int(os.environ.get("PORT", 8000))
uvicorn.run(app, host="0.0.0.0", port=port)
