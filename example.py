from dotenv import load_dotenv
import os
from pprint import pprint
from .bitrix import Bitrix24
from .tasks import TaskFields

# Загрузите переменные окружения из .env
load_dotenv()

# Получите URL вебхука Bitrix24 из переменной окружения
WEBHOOK_URL = os.getenv("webhook")

department_ids = {
    1: "Департамент 1",
    2: "Департамент 2",
    3: "Департамент 3", 
    
}

def main():
    bitrix = Bitrix24(WEBHOOK_URL)
    
    # ''' Пример получения задач по ID'''
    # task = bitrix.tasks.task.get(864883)
    # pprint(task)
    
    # ''' Пример создания новой задачи '''
    # new_task = TaskFields(
    #     TITLE="New Task from Python",
    #     DESCRIPTION="This task was created using the Bitrix24 API.",
    #     RESPONSIBLE_ID=id,  # ID пользователя, ответственного за задачу
    #     CREATED_BY=id,  # ID пользователя, создавшего задачу
    #     STATUS=2,  # Статус задачи (например, 2 - в работе)
    #     PRIORITY=3,  # Приоритет задачи (например, 3 - высокий)
    # )
    # received_task = bitrix.tasks.task.add(new_task)
    # pprint(received_task)

    # ''' Пример получения всех пользователей в списке департаментов'''
    # all_users = []
    # i = 0
    # while True:
    #     users = bitrix.user.get(
    #         FILTER = {"UF_DEPARTMENT": [key for key in department_ids.keys()], "ACTIVE": "Y"},
    #         sort= "UF_DEPARTMENT",
    #         start = len(all_users)
    #     )
    #     if not users:
    #         break
    #     all_users.extend(users)

    # birthdays = [f"{user['NAME']} {user['LAST_NAME']} {user['PERSONAL_BIRTHDAY']}" for user in all_users]
    # pprint(birthdays)
    # search = bitrix.user.search(FILTER={"FIND" : "Имя"})
    # pprint(search)
    
    # pprint(users)
if __name__ == "__main__":
    main()