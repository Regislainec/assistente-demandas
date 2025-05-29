from fastapi import FastAPI
from models import Demanda
from database import Demanda, get_all_demands

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API do Assistente de Demandas está no ar!"}

@app.post("/demandas/")
def create_demand(demanda: DemandCreate):
    return {"mensagem": "Demanda criada com sucesso"}

@app.get("/demandas/")
def listar_demandas():
    return get_all_demands()
