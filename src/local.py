import redis
from fastapi import FastAPI


app = FastAPI(
    title="Telegram Bot (private)",
    description="""
    A private server for processing requests from the local subnet and redirect them to the public server
    """
)

from src.controllers.notify import router

app.include_router(router)
