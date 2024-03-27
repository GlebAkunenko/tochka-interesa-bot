from fastapi import FastAPI
from pyteledantic.models import Bot, Update, MessageToSend

import pyteledantic.methods as tg
import src.config as config

app = FastAPI()

@app.post("/send_message")
def update_handler(update: Update):
    tg.send_message(bot.token, MessageToSend(chat_id=update.message.chat.id, text=update.message.text))
    return "OK"


bot = Bot(token="5675141206:AAHyMJbEY8GXLlq0r0-V6yfjzCeFtx4BgW4")

tg.set_webhook(bot, "/send_message")

