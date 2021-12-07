filas_celery: celery -A django_celery worker -B -Q queue_geral --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate