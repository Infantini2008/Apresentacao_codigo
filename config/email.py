from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()

# configurações de conexão com o Gmail
conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

async def enviar_email(destinatario: str, assunto: str, corpo: str):
    # monta a mensagem de email
    mensagem = MessageSchema(
        subject=assunto,
        recipients=[destinatario],
        body=corpo,
        subtype="html"
    )
    # envia o email
    fm = FastMail(conf)
    await fm.send_message(mensagem)