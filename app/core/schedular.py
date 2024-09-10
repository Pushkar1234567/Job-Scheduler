from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import logging

# Configure logging for the scheduler
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the scheduler
scheduler = BackgroundScheduler()

def dummy_job():
    logger.info(f"Dummy job executed at {datetime.now()}")

def init_scheduler():
    """Initialize the background scheduler and start it."""
    scheduler.start()
    logger.info("Scheduler started.")

def schedule_new_job(job_id: str, job_interval: str):
    """
    Schedule a new job using a cron trigger.

    :param job_id: Unique identifier for the job.
    :param job_interval: Cron expression or a predefined interval like 'mon' for every Monday.
    """
    try:
        # Example cron trigger (every Monday at 8 AM)
        cron_trigger = CronTrigger(day_of_week=job_interval, hour=8, minute=0)

        # Add the job to the scheduler
        scheduler.add_job(dummy_job, trigger=cron_trigger, id=job_id)
        logger.info(f"Job {job_id} scheduled to run every {job_interval}.")
    except Exception as e:
        logger.error(f"Error scheduling job {job_id}: {str(e)}")

def remove_job(job_id: str):
    """Remove a job from the scheduler."""
    try:
        scheduler.remove_job(job_id)
        logger.info(f"Job {job_id} removed from scheduler.")
    except Exception as e:
        logger.error(f"Error removing job {job_id}: {str(e)}")

