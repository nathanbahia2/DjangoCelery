from celery import shared_task


@shared_task
def hello_world():
    print('HELLO, WORLD!!! IT WORKET!!! ')
