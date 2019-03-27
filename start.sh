docker build -t naga .
docker run --name naga_blog \
 -p 9207:8000 \
 -dit naga

docker exec -it naga_blog python3 /root/Naga/manage.py collectstatic
docker exec -it naga_blog python3 /root/Naga/manage.py makemigrations
docker exec -it naga_blog python3 /root/Naga/manage.py migrate
docker exec -it naga_blog python3 /root/Naga/manage.py createsuperuser
docker exec -it naga_blog python3 /root/Naga/manage.py runserver 0:8000
docker exec -it naga_blog uwsgi --ini /root/Naga/uwsgi.ini