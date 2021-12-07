worker: celery -A autovist worker -l INFO -E -Q celery,queue_geral --autoscale=5,2
beat: celery -A django_celery beat -l INFO -S django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn django_celery.wsgi --log-file -
release: python manage.py migrate