../containers/wait-for-it.sh -t 60 db:5432
python manage.py migrate --noinput
python manage.py collectstatic --noinput
uwsgi --socket :8000 --mount /2015=summit/wsgi.py --processes 4 --threads 2 --manage-script-name