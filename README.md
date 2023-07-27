1. first create docker volume for pgsql persistent storage
    ```
    docker volume create [name]
    ```
    then inspect the volume to get the path to the newly created volume
    ```
    docker volume inspect [name]
    ```
    then copy the 'Mountpoint' from the output and paste it as the host volume in the docker-compose file

2. run the project `docker compose up -d --build`
3. monitor the logs of the project `docker compose logs web -f`
4. run all unit tests `docker compose exec web pytest .`
5. sample curl
```
curl --location 'http://localhost:8002/notes/' \
--header 'Content-Type: application/json' \
--data '{
    "title":"Midnight Fit3", 
    "description":"Mogwai"
}'
```
```
curl --location 'http://localhost:8002/notes/1' \
--header 'Content-Type: application/json'
```
```
curl --location 'http://localhost:8002/notes' \
--header 'Content-Type: application/json'
```