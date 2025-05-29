import sqlite3
from datetime import datetime

DB_NAME = "demandas.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS demandas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            responsavel TEXT NOT NULL,
            email_responsavel TEXT NOT NULL,
            prazo_entrega DATE NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_demand(dados):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO demandas (titulo, descricao, responsavel, email_responsavel, prazo_entrega)
        VALUES (?, ?, ?, ?, ?)
    """, (dados.titulo, dados.descricao, dados.responsavel, dados.email_responsavel, dados.prazo_entrega))
    conn.commit()
    conn.close()

def get_all_demands():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM demandas")
    results = cursor.fetchall()
    conn.close()
    return results
