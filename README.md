# Scheduler Microservice

This project is a scheduler microservice built using FastAPI and PostgreSQL. The microservice allows users to schedule jobs and provides API endpoints for managing and retrieving job details. 


## Features

- **Job Scheduling**: Schedule jobs with customizable intervals.
- **API Endpoints**:
  - `GET /jobs`: List all available jobs.
  - `GET /jobs/{id}`: Retrieve details of a specific job by ID.
  - `POST /jobs`: Create new jobs with validation.
- **Database Integration**: Stores job details like name, last run timestamp, and next run timestamp in a PostgreSQL database.
- **Scalability**: Designed to handle large-scale operations with multiple users and services.

## Project Structure

```plaintext
scheduler_microservice/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── jobs.py
│   ├── core/
│       ├── __init__.py
│       ├── scheduler.py
│
├── alembic/
├── alembic.ini
├── requirements.txt
├── README.md
