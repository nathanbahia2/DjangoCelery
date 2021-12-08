worker: celery -A django_celery worker --loglevel=info --beat & celery -A django_celery beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate