import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER", "teste@gmail.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "senha_de_teste")
SENDER_NAME = os.getenv("SENDER_NAME", "Assistente de Demandas")


def enviar_email(destinatario, assunto, mensagem):
    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = EMAIL_USER
    msg['To'] = destinatario

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
