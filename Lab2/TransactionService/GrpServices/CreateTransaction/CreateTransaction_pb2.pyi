from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestForTransaction(_message.Message):
    __slots__ = ("method", "id_user", "balance")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ID_USER_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    method: str
    id_user: int
    balance: int
    def __init__(self, method: _Optional[str] = ..., id_user: _Optional[int] = ..., balance: _Optional[int] = ...) -> None: ...

class ResponseAboutTransaction(_message.Message):
    __slots__ = ("status", "report")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    report: str
    def __init__(self, status: bool = ..., report: _Optional[str] = ...) -> None: ...
