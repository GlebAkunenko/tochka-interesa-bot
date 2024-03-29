from fastapi import FastAPI
from pyteledantic.models import Update, MessageToSend

import pyteledantic.methods as tg
import src.config as config
import src.utils as bot

app = FastAPI(
    title="Telegram Bot (public)",
    description="""
    A public server for processing requests from the WWW via webhooks
    """
)


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
    return tg.get_webhook_info(bot.token)


@app.on_event("startup")
async def on_start():
    tg.set_webhook(bot.token, config.webhook_url, config.ssl_certfile)
    await bot.notify_moderators("✅ Бот запущен ✅")


@app.on_event("shutdown")
async def on_stop():
    tg.delete_webhook(bot.token)
    await bot.notify_moderators("❌ Бот остановлен ❌")
