# python-server
HTTP Server to expose a web directory to serve different files for a configurable amount of requests.
## Build Status

| Build                                     | Status               
| ----------------------------------------- | -------------------
| python-server (master                                  | [![Build Status](https://dev.azure.com/samliniger/python-server/_apis/build/status/samliniger.python-server?branchName=master)](https://dev.azure.com/samliniger/python-server/_build/latest?definitionId=1&branchName=master)
| python-server (master                                  | [![Build Status](https://dev.azure.com/samliniger/python-server/_apis/build/status/samliniger.python-server?branchName=dev)](https://dev.azure.com/samliniger/python-server/_build/latest?definitionId=1&branchName=dev)

# How-to
Start the server

```console
docker-compose up
```
Without docker compose

```console
docker build -t python-server .
docker run -it --rm -p 80:8000  -e "REQUEST_LIMIT=2" -v $PWD/web/:/usr/src/app/web --name running-server python-server
```
