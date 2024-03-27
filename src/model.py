from pydantic import BaseModel

import datetime as dt

class Moderator(BaseModel):
    id: int
    name: str
    telegram_id: str
    is_superuser: bool
    hiring_date: dt.datetime

