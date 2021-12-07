filas_celery: celery -A django_celery worker -E --l INFO --beat --l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate