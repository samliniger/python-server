FROM python:2-alpine

WORKDIR /usr/src/app

ADD ./server.py .
EXPOSE 8000
CMD [ "python", "./server.py" ]
