from sqlalchemy import Column, String, DateTime
from .database import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    interval = Column(String)
    last_run = Column(DateTime, nullable=True)
    next_run = Column(DateTime, nullable=True)
        