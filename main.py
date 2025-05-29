from fastapi import FastAPI
from models import DemandCreate
from database import create_demand, get_all_demands

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API do Assistente de Demandas está no ar!"}

@app.post("/demandas/")
def criar_demanda(demanda: DemandCreate):
    create_demand(demanda)
    return {"mensagem": "Demanda criada com sucesso"}

@app.get("/demandas/")
def listar_demandas():
    return get_all_demands()
