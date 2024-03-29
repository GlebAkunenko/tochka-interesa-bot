from pyteledantic.models import Message
from pythonping import ping

from src.handlers.base import Handler
from src.config import servers
from src.utils import send_message

import datetime as dt

handler = Handler()


@handler.command('/chechup')
@handler.command('Состояние серверов')
def check(message: Message):
    user = message.from_user.id
    statuses = []
    for server in servers:
        result = ping(server[1], count=1)
        statuses.append(result.success())
    text = ""
    for i in range(len(servers)):
        text += f"{servers[i][0].rjust(30)} {'✅' if statuses[i] else '❌'}\n"
    send_message(user, text)
