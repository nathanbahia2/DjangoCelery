filas_celery: celery -A django_celery worker -E -Q queue_geral --beat -l=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate