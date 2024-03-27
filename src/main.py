from fastapi import FastAPI
from pyteledantic.models import Bot, Update, MessageToSend

import pyteledantic.methods as tg
import src.config as config

app = FastAPI()
bot = Bot(token=config.token)


@app.post("/send_message")
def update_handler(update: Update):
    tg.send_message(bot.token, MessageToSend(chat_id=update.message.chat.id, text=update.message.text))
    return "OK"


@app.get("/info")
def get_info():
    return tg.get_webhook_info(bot)


@app.on_event("startup")
def on_start():
    tg.set_webhook(bot, config.webhook_url, config.ssl_certfile)


@app.on_event("shutdown")
def on_stop():
    tg.delete_webhook(bot)
