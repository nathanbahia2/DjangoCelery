import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'example-task': {
        'task': 'apps.inspirations.tasks.hello_world',
        'schedule': 5.0,  # every five seconds
    },
}
