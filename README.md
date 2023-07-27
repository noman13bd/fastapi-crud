1. first create docker volume for pgsql persistent storage
    ```
    docker volume create [name]
    ```
    then inspect the volume to get the path to the newly created volume
    ```
    docker volume inspect [name]
    ```
    then pull the 'Mountpoint' from the output and paste it as the host volume in the docker-compose file

2. run the project `docker compose up -d --build`
3. monitor the logs of the project `docker compose logs web -f`
4. run all unit tests `docker compose exec web pytest .`