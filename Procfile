worker: celery --app django_celery worker --loglevel info --beat
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate