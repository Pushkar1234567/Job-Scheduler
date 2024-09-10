from sqlalchemy.orm import Session
from .models import Job
from .schemas import JobCreate

def get_jobs(db: Session):
    return db.query(Job).all()

def get_job(db: Session, job_id: str):
    return db.query(Job).filter(Job.id == job_id).first()

def create_job(db: Session, job: JobCreate):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
