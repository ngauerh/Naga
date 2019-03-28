docker build -t naga .
docker run --name naga_blog \
 -p 9208:8000 \
 -dit naga

docker exec -it naga_blog python3 /home/www-data/Naga/manage.py collectstatic
docker exec -it naga_blog python3 /home/www-data/Naga/manage.py makemigrations
docker exec -it naga_blog python3 /home/www-data/Naga/manage.py migrate
docker exec -it naga_blog python3 /home/www-data/Naga/manage.py createsuperuser
docker exec -it naga_blog supervisord
docker exec -it naga_blog /etc/init.d/nginx restart
docker exec -it naga_blog supervisorctl restart naga