from fastapi import FastAPI
from pyteledantic.models import Update

import pyteledantic.methods as tg
import src.config as config

from src.utils import Bot

app = FastAPI(
    title="Telegram Bot (public)",
    description="""
    A public server for processing requests from the WWW via webhooks
    """
)
bot = Bot(config.token)


from src.handlers.moderators import handler as moderator

handlers = [] + moderator.funcs

@app.post("/send_message")
def update_handler(update: Update):
    for handler in handlers:
        answer = handler(update)
        if answer:
            bot.send_message(update.message.from_user.id, answer)
            return
    if update.message:
        bot.send_message(update.message.from_user.id, "Неизвестная команда")


@app.get("/info")
def get_info():
    return tg.get_webhook_info(bot)


@app.on_event("startup")
def on_start():
    tg.set_webhook(bot, config.webhook_url, config.ssl_certfile)


@app.on_event("shutdown")
def on_stop():
    tg.delete_webhook(bot)
