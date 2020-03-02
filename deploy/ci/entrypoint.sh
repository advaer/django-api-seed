#!/usr/bin/env bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Run server
gunicorn --reload \
         --timeout=300 \
         --bind=0.0.0.0:5000 \
         --forwarded-allow-ips 127.0.0.1 \
         --log-config .gunicorn-logging.ini \
         --worker-class=sync \
         --workers=5 \
         --threads=1 \
         --name=django_api_seed \
         --pythonpath src
