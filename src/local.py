import redis
from fastapi import FastAPI

from src.utils import notify_moderators


app = FastAPI(
    title="Telegram Bot (private)",
    description="""
    A private server for processing requests from the local subnet and redirect them to the public server
    """
)


@app.on_event("startup")
async def on_start():
    await notify_moderators("✅ Регистратор сообщений запущен ✅")


@app.on_event("shutdown")
async def on_stop():
    await notify_moderators("❌ Регистратор сообщений остановлен ❌")



from src.controllers.notify import router

app.include_router(router)
