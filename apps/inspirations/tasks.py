from datetime import datetime

from django_celery.celery import app
from celery.utils.log import get_task_logger

from apps.inspirations.models import Message


logger = get_task_logger(__name__)


@app.task(name="task_hello_world", queue="queue_geral")
def hello_world(*args, **kwargs):
    logger.info(args)
    logger.info(kwargs)
    Message.objects.create(
        author='CELERY',
        message=f'IT WORKET!!! IT"S { datetime.now().isoformat() } RIGHT NOW'
    )
