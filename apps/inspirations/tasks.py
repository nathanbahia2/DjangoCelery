from datetime import datetime

from django_celery.celery import app


@app.task(name="task_hello_world", queue="queue_hello_world")
def hello_world():
    print(f'HELLO, WORLD!!! IT WORKET!!! IT"S { datetime.now().isoformat() } RIGHT NOW')
