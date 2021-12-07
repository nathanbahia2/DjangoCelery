filas_celery: celery --app django_celery worker -E -Q queue_geral --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate