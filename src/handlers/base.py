from pyteledantic.models import Update

class Handler:
    def __init__(self):
        self.funcs = []


    def command(self, command):
        def decorator(func):
            def wrapper(update: Update) -> bool:
                if update.message and update.message.text and update.message.text.startswith(command):
                    func(update.message)
                    return True
                return False
            self.funcs.append(wrapper)
            return wrapper
        return decorator

