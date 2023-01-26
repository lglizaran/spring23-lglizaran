#!/bin/bash
echo 'cd into lab1'
cd ./lab1 

echo 'Building image'
docker build . -t lab1_image

echo 'launch app'
docker run --name lab1_container -d -p 8000:8000 lab1_image

echo "waiting for API to be launched"
timeout 300 bash -c 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' http://localhost:8000)" != "501" ]]; do sleep 5; done' || false

echo "testing '/hello' endpoint with ?name=Winegar"
curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/hello?name=Winegar"

echo "testing '/' endpoint"
curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/"

echo "testing '/docs' endpoint"
curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/docs"

echo 'stop container'
docker stop lab1_container

echo 'delete container'
docker rm lab1_container