filas_celery: celery -A django_celery worker --beat --scheduler django --loglevel=info
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate