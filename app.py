import streamlit as st
import requests

st.title("Assistente de Demandas")

api_url = "https://seu-backend.herokuapp.com"  # ou URL local para testes

if "token" not in st.session_state:
    st.session_state.token = ""

st.text_input("Título da demanda", key="titulo")
st.text_input("Email do responsável", key="email")
if st.button("Criar demanda"):
    payload = {
        "titulo": st.session_state.titulo,
        "email_responsavel": st.session_state.email,
    }
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    response = requests.post(f"{api_url}/demandas", json=payload, headers=headers)
    if response.status_code == 200:
        st.success("Demanda criada com sucesso!")
    else:
        st.error("Erro ao criar demanda.")
