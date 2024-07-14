from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    title: str
    description: str
    status: bool = False
    is_deleted: bool = False
    created: int = int(datetime.timestamp(datetime.now()))
    updated: int = int(datetime.timestamp(datetime.now()))