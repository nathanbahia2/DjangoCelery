filas_celery: celery -A django_celery -E worker --loglevel=info --beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate