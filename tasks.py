from dataclasses import dataclass, field
from typing import Optional, List, Any
from .method import Method

    
@dataclass
class TaskFields:
    ID: Optional[int] = None
    PARENT_ID: int = 0
    TITLE: str = ""
    DESCRIPTION: Optional[str] = None
    MARK: Optional[str] = None  # 'N', 'P', or None
    PRIORITY: int = 1  # 2, 1, 0
    STATUS: int = 2  # 2, 3, 4, 5, 6
    MULTITASK: Optional[str] = None  # 'Y', 'N'
    NOT_VIEWED: Optional[str] = None  # 'Y', 'N'
    REPLICATE: Optional[str] = None  # 'Y', 'N'
    GROUP_ID: int = 0
    FLOW_ID: Optional[int] = None
    STAGE_ID: int = 0
    CREATED_BY: Optional[int] = None
    CREATED_DATE: Optional[str] = None  # ISO datetime string
    RESPONSIBLE_ID: Optional[int] = None
    ACCOMPLICES: List[int] = field(default_factory=list)
    AUDITORS: List[int] = field(default_factory=list)
    CHANGED_BY: Optional[int] = None
    CHANGED_DATE: Optional[str] = None
    STATUS_CHANGED_BY: Optional[int] = None
    CLOSED_BY: Optional[int] = None
    CLOSED_DATE: Optional[str] = None
    DATE_START: Optional[str] = None
    DEADLINE: Optional[str] = None
    START_DATE_PLAN: Optional[str] = None
    END_DATE_PLAN: Optional[str] = None
    GUID: Optional[str] = None
    XML_ID: Optional[str] = None
    COMMENTS_COUNT: Optional[int] = None
    NEW_COMMENTS_COUNT: Optional[int] = None
    ALLOW_CHANGE_DEADLINE: Optional[str] = None  # 'Y', 'N'
    ALLOW_TIME_TRACKING: Optional[str] = None  # 'Y', 'N'
    TASK_CONTROL: Optional[str] = None  # 'Y', 'N'
    ADD_IN_REPORT: Optional[str] = None  # 'Y', 'N'
    FORKED_BY_TEMPLATE_ID: Optional[str] = None  # 'Y', 'N'
    TIME_ESTIMATE: Optional[int] = None
    TIME_SPENT_IN_LOGS: Optional[int] = None
    MATCH_WORK_TIME: Optional[int] = None
    FORUM_TOPIC_ID: Optional[int] = None
    FORUM_ID: Optional[int] = None
    SITE_ID: Optional[str] = None
    SUBORDINATE: Optional[str] = None  # 'Y', 'N'
    FAVORITE: Optional[str] = None  # 'Y', 'N'
    EXCHANGE_MODIFIED: Optional[str] = None
    EXCHANGE_ID: Optional[int] = None
    OUTLOOK_VERSION: Optional[int] = None
    VIEWED_DATE: Optional[str] = None
    SORTING: Optional[float] = None
    DURATION_PLAN: Optional[int] = None
    DURATION_FACT: Optional[int] = None
    CHECKLIST: List[Any] = field(default_factory=list)
    DURATION_TYPE: str = "days"  # 0-6
    UF_CRM_TASK: Optional[List[str]] = None
    UF_TASK_WEBDAV_FILES: Optional[List[Any]] = None
    UF_MAIL_MESSAGE: Optional[Any] = None
    IS_MUTED: Optional[str] = None  # 'Y', 'N'
    IS_PINNED: Optional[str] = None  # 'Y', 'N'
    IS_PINNED_IN_GROUP: Optional[str] = None  # 'Y', 'N'
    SERVICE_COMMENTS_COUNT: Optional[int] = None

class TasksTask(Method):
    def __init__(self, webhook_url):
        super().__init__(webhook_url)
        self.files_attach = "tasks.task.files.attach"
        self.delegate = "tasks.task.delegate"
        self.counters_get = "tasks.task.counters.get"
        self.start = "tasks.task.start"
        self.pause = "tasks.task.pause"
        self.defer = "tasks.task.defer"
        self.complete = "tasks.task.complete"
        self.renew = "tasks.task.renew"
        self.approve = "tasks.task.approve"
        self.disapprove = "tasks.task.disapprove"
        self.delete = "tasks.task.delete"
        self.startwatch = "tasks.task.startwatch"
        self.stopwatch = "tasks.task.stopwatch"
        self.favorite_add = "tasks.task.favorite.add"
        self.favorite_remove = "tasks.task.favorite.remove"
        self.getFields = "tasks.task.getFields"
        self.getaccess = "tasks.task.getaccess"
        self.history_list = "tasks.task.history.list"
        self.mute = "tasks.task.mute"
        self.unmute = "tasks.task.unmute"

    def add(self, task : TaskFields) -> TaskFields:
        return self.send_method(metod='tasks.task.add', fields={"fields": task.__dict__})
    
    def update(self, task_id: int, task: TaskFields) -> TaskFields:
        return self.send_method(metod='tasks.task.update', fields={"taskId": task_id, "fields": task.__dict__})
    
    def get(self, task_id: int) -> TaskFields:
        return self.send_method(metod='tasks.task.get', fields={"taskId": task_id})
    
    def list(self, filter: Optional[dict] = None, select: Optional[List[str]] = None) -> List[TaskFields]:
        fields = {}
        if filter:
            fields['filter'] = filter
        if select:
            fields['select'] = select
        result = self.send_method(metod='tasks.task.list', fields=fields)
        result.raise_for_status()
        return result.get('result', [])

class Tasks:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.task = TasksTask(webhook_url)


   

