from pyteledantic.models import MessageToSend
import pyteledantic.methods as tg

class Bot:
    def __init__(self, token: str):
        self.token = token

    def send_message(self, user: int, text: str):
        tg.send_message(self.token, MessageToSend(chat_id=user, text=text))