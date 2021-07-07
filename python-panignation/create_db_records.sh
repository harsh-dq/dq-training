!/bin/bash
x=1
while [ $x -le 100 ]
do
  curl -X POST -H "Content-Type: application/json" -d '{ "email": "man@123.com", "firstname": "man", "lastname": "man", "comments": "hello there" }' http://0.0.0.0:8080/
  sleep 1s
  x=$(( $x + 1 ))
done