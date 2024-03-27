from pydantic_redis import Model, Store, RedisConfig

import datetime as dt

store = Store(
    name="bot-store",
    redis_config=RedisConfig(host="localhost", port=6379)
)


class Moderator(Model):
    _primary_key_field: str = "telegram_id"
    name: str
    username: str
    telegram_id: int
    is_superuser: bool
    hiring_date: dt.datetime


store.register_model(Moderator)