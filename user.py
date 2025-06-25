from .method import Method
from dataclasses import dataclass
from typing import TypedDict, Literal, Union, List, Optional, Any


@dataclass
class UserFields:
    EMAIL: str = ""
    NAME: str = ""
    LAST_NAME: str = ""
    SECOND_NAME: str = ""
    PERSONAL_GENDER: str = ""  # 'M', 'F', or ''
    PERSONAL_PROFESSION: str = ""
    PERSONAL_WWW: str = ""
    PERSONAL_BIRTHDAY: str = ""
    PERSONAL_PHOTO: list = None
    PERSONAL_ICQ: str = ""
    PERSONAL_PHONE: str = ""
    PERSONAL_FAX: str = ""
    PERSONAL_MOBILE: str = ""
    PERSONAL_PAGER: str = ""
    PERSONAL_STREET: str = ""
    PERSONAL_CITY: str = ""
    PERSONAL_STATE: str = ""
    PERSONAL_ZIP: str = ""
    PERSONAL_COUNTRY: str = ""
    PERSONAL_MAILBOX: str = ""
    PERSONAL_NOTES: str = ""
    WORK_PHONE: str = ""
    WORK_COMPANY: str = ""
    WORK_POSITION: str = ""
    WORK_DEPARTMENT: str = ""
    WORK_WWW: str = ""
    WORK_FAX: str = ""
    WORK_PAGER: str = ""
    WORK_STREET: str = ""
    WORK_MAILBOX: str = ""
    WORK_CITY: str = ""
    WORK_STATE: str = ""
    WORK_ZIP: str = ""
    WORK_COUNTRY: str = ""
    WORK_PROFILE: str = ""
    WORK_LOGO: list = None
    WORK_NOTES: str = ""
    UF_SKYPE_LINK: str = ""
    UF_ZOOM: str = ""
    UF_DEPARTMENT: str = ""
    UF_INTERESTS: str = ""
    UF_SKILLS: str = ""
    UF_WEB_SITES: str = ""
    UF_XING: str = ""
    UF_LINKEDIN: str = ""
    UF_FACEBOOK: str = ""
    UF_TWITTER: str = ""
    UF_SKYPE: str = ""
    UF_DISTRICT: str = ""
    UF_PHONE_INNER: str = ""

class SearchFilter(TypedDict, total=False):
    NAME: str
    LAST_NAME: str
    WORK_POSITION: str
    UF_DEPARTMENT_NAME: str
    USER_TYPE: Literal["employee", "extranet", "email"]
    FIND: str


class User(Method):
    def __init__(self, webhook_url):
        super().__init__(webhook_url)

    def fields(self):
        return self.send_method(metod='user.fields')
    
    def current(self) -> UserFields:
        return self.send_method(metod='user.current')
    
    def add(self, fields: UserFields) -> UserFields:
        return self.send_method(metod='user.add', fields=fields)
    
    def update(self, fields: UserFields) -> UserFields:
        return self.send_method(metod='user.update', fields=fields)
    
    def get(self, sort="NAME", order='ASC', FILTER={}, ADMIN_MODE='N', start=0) -> list[UserFields]:
        fields = {
            'sort': sort,
            'order': order,
            'FILTER': FILTER,
            'ADMIN_MODE': ADMIN_MODE,
            'start': start
        }

        return self.send_method(metod='user.get', fields=fields)
    
    def search(
        self,
        FILTER: Optional[SearchFilter] = None,
        sort: str = "",
        order: str = "ASC",
        ADMIN_MODE: str = 'N',
        start: int = 0
    ) -> list[UserFields]:
        FILTER = FILTER or {}
        allowed_keys = set(SearchFilter.__annotations__.keys())
        for key in FILTER:
            if key not in allowed_keys:
                raise ValueError(f"Недопустимое поле фильтра: {key}")
        if "FIND" in FILTER and len(FILTER) > 1:
            raise ValueError("Если используется FIND, нельзя указывать другие поля фильтра.")
        return self.send_method(
            metod='user.search',
            fields={'FILTER': FILTER, 'sort': sort, 'order': order, 'ADMIN_MODE': ADMIN_MODE, 'start': start}
        )