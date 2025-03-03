import os
from dotenv import load_dotenv
import telebot


# Carrega o .env somente se estiver rodando localmente
if os.getenv('RAILWAY_ENVIRONMENT') is None:
    load_dotenv()

# Lê as variáveis de ambiente
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def enviar_mensagem(mensagem, CHAT_ID = '5588207726',BOT_TOKEN = os.getenv('BOT_TOKEN')):

    bot = telebot.TeleBot(BOT_TOKEN)

    # Enviando a mensagem
    bot.send_message(CHAT_ID, mensagem)
