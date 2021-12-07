worker: celery -A django_celery worker --beat -S django --l info
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate