#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace


python webboard/manage.py migrate
python webboard/manage.py runserver 0.0.0.0:8000
