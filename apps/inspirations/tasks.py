from datetime import datetime

from django_celery.celery import app


@app.task(name="task_hello_world", queue="queue_geral")
def hello_world(*args, **kwargs):
    print(f'HELLO, WORLD!!! IT WORKET!!! IT"S { datetime.now().isoformat() } RIGHT NOW')
    print(args)
    print(kwargs)
