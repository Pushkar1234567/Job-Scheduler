
from fastapi import FastAPI
from app.routers import jobs
from app.core.scheduler import init_scheduler
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Initialize scheduler
init_scheduler()

# Include routers
app.include_router(jobs.router)
