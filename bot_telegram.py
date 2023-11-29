from config import *
from numero_de_lote import *
import telebot
import threading

bot = telebot.TeleBot(telegram_token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Hola")


@bot.message_handler(commands=["lote"])
def cmd_start(message):
    bot.reply_to(message, lote)


@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        bot.send_message(message.chat.id, "Insertar comando")


def recibir_mensajes():
    bot.infinity_polling()


if __name__ == '__main__':
    print("Bot starting")
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
