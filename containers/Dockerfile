FROM python:2.7.9

RUN apt-get update

RUN apt-get install -y nodejs npm

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN pip install uwsgi==2.0.15

ADD /requirements /app/requirements

RUN pip install -r /app/requirements/production.txt

RUN npm install -g node-sass bower

ADD / /app

WORKDIR /app/summit/static

RUN bower --allow-root install

WORKDIR /app/summit

CMD ../containers/run.sh