celery: celery --app django_celery worker --loglevel info --beat & wait -n; celery -app django_celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate