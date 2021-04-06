#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
