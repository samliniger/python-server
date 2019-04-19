# python-server
Start the server

```console
docker-compose up
```
Without docker compose

```console
docker build -t python-server .
docker run -it --rm -p 80:8000  -v $PWD/web/:/usr/src/app/web --name running-server python-server
```