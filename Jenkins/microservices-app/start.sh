#! bin/bash
docker network create app

docker build -t ishu0824/routing:$1 ${pwd}/routing/.
docker build -t ishu0824/userservice:$1 ${pwd}/user-service/.
docker build -t ishu0824/orderservice:$1 ${pwd}/user-service/.


docker run -d -p 80:80 --name --net app routing ishu0824/routing:$1
docker run -d -p 3000-3000 --name --net app userservice ishu0824/userservice:$1
docker run -d -p 3001:3001 --name --net app orderservice ishu0824/orderservice:$1