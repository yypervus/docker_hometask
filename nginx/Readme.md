docker build -t my_nginx .
docker run -d -p 80:80 --rm --name new_nginx my_nginx 
