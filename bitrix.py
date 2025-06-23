from tasks import Tasks
from user import User

class Bitrix24:
    def __init__(self, webhook_url: str):
        self.tasks = Tasks(webhook_url)
        self.user = User(webhook_url)


