#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput
# Apply database migrations
echo "Apply database migrations"
python makemigrations
python manage.py migrate


exec "$@"