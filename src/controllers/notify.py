from fastapi.routing import APIRouter

from src.model import Moderator

import src.utils as bot

router = APIRouter(prefix="/notify")


@router.post("/server")
async def server_status(server: str, is_active: bool):
    text = f"{'✅' if is_active else '❌'} *{server}* {'запущен ✅' if is_active else 'остановлен ❌'}"
    await bot.notify_moderators(text)
