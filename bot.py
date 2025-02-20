import telebot

TOKEN = "SEU_TOKEN_DO_BOT"
bot = telebot.TeleBot(TOKEN)

# Lista de times disponíveis
TIMES = [
    "ABC", "América-MG", "Amazonas", "Athletico", "Atlético-GO", "Atlético-MG", "Avaí", "Bahia",
    "Botafogo", "Botafogo-SP", "Chapecoense", "Ceará", "Corinthians", "CRB", "Cruzeiro", "Criciúma",
    "Cuiabá", "Figueirense", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Grêmio", "Guarani",
    "Internacional", "Ituano", "Juventude", "Londrina", "Mirassol", "Náutico", "Novorizontino",
    "Operário", "Palmeiras", "Ponte Preta", "Red Bull Bragantino", "Santos", "São Paulo",
    "Sampaio Corrêa", "Sport", "Tombense", "Vila Nova", "Vitória", "Vasco"
]

usuarios = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 Olá! Escolha seu time enviando: /time NomeDoTime")

@bot.message_handler(commands=['time'])
def escolher_time(message):
    time = message.text.replace("/time ", "").strip()
    if time in TIMES:
        usuarios[message.chat.id] = time
        bot.send_message(message.chat.id, f"✅ Seu time foi definido como {time}.")
    else:
        bot.send_message(message.chat.id, "⚽ Time inválido! Escolha um dos seguintes:\n" + ", ".join(TIMES))

bot.polling()