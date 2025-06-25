## Реализованные методы
> Первый чекбокс — реализовано, второй — протестировано. 

<details>
<summary><b>user | Пользователи</b></summary>

- [x] | [x] **user.fields** — Получение структуры полей пользователя
- [x] | [x] **user.current** — Получение текущего пользователя
- [x] | [x] **user.add** — Добавление пользователя
- [x] | [x] **user.update** — Обновление пользователя
- [x] | [x] **user.get** — Получение списка пользователей с фильтрацией
- [x] | [x] **user.search** — Поиск пользователей по фильтру

</details>

<details>
<summary><b>tasks | Задачи</b></summary>

- [x] [x] **tasks.task.add** — Создание задачи
- [x] [x] **tasks.task.update** — Обновление задачи
- [x] [x] **tasks.task.get** — Получение задачи по ID
- [x] [x] **tasks.task.list** — Получение списка задач
- [ ] [ ] **tasks.task.delete** — Удаление задачи
- [ ] [ ] **tasks.task.complete** — Завершение задачи
- [ ] [ ] **tasks.task.pause** — Пауза задачи
- [ ] [ ] **tasks.task.start** — Запуск задачи
- [ ] [ ] **tasks.task.defer** — Отложить задачу
- [ ] [ ] **tasks.task.renew** — Возобновить задачу
- [ ] [ ] **tasks.task.approve** — Принять задачу
- [ ] [ ] **tasks.task.disapprove** — Отклонить задачу
- [ ] [ ] **tasks.task.favorite.add** — Добавить задачу в избранное
- [ ] [ ] **tasks.task.favorite.remove** — Удалить задачу из избранного
- [ ] [ ] **tasks.task.getFields** — Получить структуру полей задачи
- [ ] [ ] **tasks.task.getaccess** — Получить права доступа к задаче
- [ ] [ ] **tasks.task.history.list** — История изменений задачи
- [ ] [ ] **tasks.task.mute** — Отключить уведомления по задаче
- [ ] [ ] **tasks.task.unmute** — Включить уведомления по задаче

</details>

<details>
<summary><b>task | Задача</b></summary>
<details>
<summary><b>commentitem | Комментарии к задачам </b></summary>

- [x] [x] **task.commentitem.add** — Добавить комментарий к задаче
- [x] [x] **task.commentitem.update** — Обновить комментарий к задаче
- [x] [x] **task.commentitem.get** — Получить комментарий по ID
- [x] [x] **task.commentitem.getlist** — Получить список комментариев к задаче
- [x] [x] **task.commentitem.delete** — Удалить комментарий к задаче
- [x] [x] **task.commentitem.isactionallowed** — Проверить разрешение действия с комментарием
- [x] [ ] **task.commentitem.getmanifest** — Получить манифест комментария

</details>

<details>
<summary><b>taskresult | Результаты задач</b></summary>

- [x] [ ] **tasks.task.taskresult.addFromComment** — Добавить результат задачи из комментария
- [x] [ ] **tasks.task.taskresult.list** — Получить список результатов задачи
- [x] [ ] **tasks.task.taskresult.deleteFromComment** — Удалить результат задачи из комментария

</details>
</details>
