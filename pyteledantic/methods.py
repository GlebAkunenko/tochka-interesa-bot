import requests
from asynchronous_requests import request

from pyteledantic.exceptions.exceptions import TelegramAPIException
from pyteledantic.models import Bot, Message, MessageToSend, User, WebhookInfo
from pyteledantic.utils import base_method


def get_me(bot: Bot) -> User:
    url = f'https://api.telegram.org/bot{bot.token}/getMe'
    user = base_method(url, response_model=User)
    assert isinstance(user, User)
    return user


def get_webhook_info(token: str) -> WebhookInfo:
    url = f'https://api.telegram.org/bot{token}/getWebhookInfo'
    webhook_info = base_method(url, response_model=WebhookInfo)
    assert isinstance(webhook_info, WebhookInfo)
    return webhook_info


def set_webhook(token: str, webhook_url: str, cert_path: str) -> bool:
    url = 'https://api.telegram.org/bot{}/setWebhook?url={}'
    url = url.format(token, webhook_url)
    session = requests.Session()
    files = {'certificate': open(cert_path, 'rb')}
    response = session.request("POST", url, files=files)
    if response.status_code == 200:
        return True
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)


def delete_webhook(token: str) -> bool:
    url = f'https://api.telegram.org/bot{token}/deleteWebhook'
    result = base_method(url)
    assert isinstance(result, bool)
    return result


def send_message(token: str, message: MessageToSend) -> Message:
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    msg = base_method(url,
                      method='POST',
                      params=message.dict(),
                      response_model=Message)
    assert isinstance(msg, Message)
    return msg


async def send_message_async(token: str, message: MessageToSend) -> Message:
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    msg = await request('POST', url, params=message.dict(), response_model=Message)
    assert isinstance(msg, Message)
    return msg


