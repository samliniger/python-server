FROM python:3-alpine

WORKDIR /usr/src/app

ADD ./server.py .
EXPOSE 8000
CMD [ "python", "./server.py" ]
