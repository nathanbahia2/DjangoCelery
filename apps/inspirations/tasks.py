from datetime import datetime

from django_celery.celery import app
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@app.task(name="task_hello_world", queue="queue_geral")
def hello_world(*args, **kwargs):
    logger.info(f'HELLO, WORLD!!! IT WORKET!!! IT"S { datetime.now().isoformat() } RIGHT NOW')
    logger.info(args)
    logger.info(kwargs)
