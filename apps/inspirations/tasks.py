from django_celery.celery import app


@app.task
def hello_world():
    print('Hello World! It Worked!!! ')
