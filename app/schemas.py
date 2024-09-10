from pydantic import BaseModel
from datetime import datetime

class JobBase(BaseModel):
    name: str
    interval: str

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: str
    last_run: datetime = None
    next_run: datetime = None

    class Config:
        orm_mode = True
