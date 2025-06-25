from .tasks import Tasks, Task
from .user import User

class Bitrix24:
    def __init__(self, webhook_url: str):
        self.tasks = Tasks(webhook_url)
        self.task = Task(webhook_url)
        self.user = User(webhook_url)
        

