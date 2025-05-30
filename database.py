from models import Demanda
from typing import List
import sqlite3

def create_demand(demanda: Demanda):
    conn = sqlite3.connect("demandas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS demandas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            descricao TEXT,
            nome_responsavel TEXT,
            email_responsavel TEXT,
            prioridade TEXT,
            prazo_entrega TEXT,
            status TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO demandas (titulo, descricao, nome_responsavel, email_responsavel, prioridade, prazo_entrega, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        demanda.titulo,
        demanda.descricao,
        demanda.nome_responsavel,
        demanda.email_responsavel,
        demanda.prioridade,
        str(demanda.prazo_entrega),
        demanda.status
    ))
    conn.commit()
    conn.close()
    return {"mensagem": "Demanda criada com sucesso"}

def get_all_demanda() -> List[Demanda]:
    conn = sqlite3.connect("demandas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, descricao, nome_responsavel, email_responsavel, prioridade, prazo_entrega, status FROM demandas")
    rows = cursor.fetchall()
    conn.close()
    return [Demanda(
        titulo=row[0],
        descricao=row[1],
        nome_responsavel=row[2],
        email_responsavel=row[3],
        prioridade=row[4],
        prazo_entrega=row[5],
        status=row[6]
    ) for row in rows]
