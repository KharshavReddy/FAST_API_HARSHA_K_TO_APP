from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    content: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    description : str

    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
