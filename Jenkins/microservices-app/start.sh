#! bin/bash
docker network create app

docker build -t ishu0824/routing:$1 Jenkins/microservices-app/routing/.
docker build -t ishu0824/userservice:$1 Jenkins/microservices-app/user-service/.
docker build -t ishu0824/orderservice:$1 Jenkins/microservices-app/user-service/.


docker rm -f routing userservice orderservice
docker run -d -p 80:80  --net app --name routing ishu0824/routing:$1
docker run -d -p 3000-3000  --net app --name userservice ishu0824/userservice:$1
docker run -d -p 3001:3001  --net app --name orderservice ishu0824/orderservice:$1