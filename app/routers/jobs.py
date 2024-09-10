from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import JobCreate, JobResponse
from app.crud import get_jobs, get_job, create_job
from app.database import get_db
from app.core.scheduler import schedule_new_job
from typing import List

router = APIRouter()

@router.get("/jobs", response_model=List[JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    return get_jobs(db)

@router.get("/jobs/{job_id}", response_model=JobResponse)
def retrieve_job(job_id: str, db: Session = Depends(get_db)):
    job = get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/jobs", response_model=JobResponse)
def create_new_job(job: JobCreate, db: Session = Depends(get_db)):
    job_data = create_job(db, job)
    schedule_new_job(job_data.id, job_data.interval)
    return job_data
