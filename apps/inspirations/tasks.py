from django_celery.celery import app


@app.task(name="First Celery Task")
def hello_world():
    print('HELLO, WORLD!!! IT WORKET!!! ')
