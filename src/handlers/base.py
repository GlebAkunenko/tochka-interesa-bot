from pyteledantic.models import Update

class Handler:
    def __init__(self, func):
        self.func = func

    def is_approach(self, update: Update):
        return True


class Command(Handler):
    def __init__(self, command, func):
        super().__init__(func)
        self.command = command

    def is_approach(self, update: Update):
        if update.message:
            if update.message.text:
                return update.message.text.startswith(self.command)
        return False


handlers: list[Handler] = []


def command_handler(command: str):
    def decorator(func):
        def wrapper(update: Update):
            return func(update.message)
        handlers.append(Command(command, wrapper))
        return func
    return decorator