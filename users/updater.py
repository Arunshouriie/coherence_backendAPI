from apscheduler.schedulers.background import BackgroundScheduler
from .dispense import process_schedule
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

executors = {
    'default': ThreadPoolExecutor(1),
    'processpool': ProcessPoolExecutor(1)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

def start():
    scheduler = BackgroundScheduler(job_defaults= job_defaults, executors=executors)
    scheduler.add_job(process_schedule, 'interval', seconds=10)
    scheduler.start()