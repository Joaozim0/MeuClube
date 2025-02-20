import telebot
import requests

TOKEN = "7098786378:AAFrxaj8sYFZrwVN3o8S7v7pyWvtSLzZ3DI"
bot = telebot.TeleBot(TOKEN)

# Dicionário para armazenar o time escolhido pelos usuários
usuarios = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Olá! Escolha seu time digitando: /time NomeDoTime")

@bot.message_handler(commands=['time'])
def escolher_time(message):
    time = message.text.replace("/time ", "").strip()
    if time:
        usuarios[message.chat.id] = time
        bot.send_message(message.chat.id, f"Seu time foi definido como {time}. Você receberá notícias e resultados ao vivo.")
    else:
        bot.send_message(message.chat.id, "Por favor, informe o nome do seu time após o comando /time.")

# Função para enviar atualizações
def enviar_atualizacoes():
    while True:
        for user_id, time in usuarios.items():
            # Aqui você pode integrar uma API de futebol (Exemplo: API-Football) para buscar notícias e placares ao vivo
            bot.send_message(user_id, f"🔔 Atualização do {time}: Nenhuma nova informação no momento.")  
        time.sleep(60)  # Atualiza a cada 60 segundos

import threading
threading.Thread(target=enviar_atualizacoes).start()

bot.polling()
