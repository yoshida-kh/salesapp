FROM python:3.7-alpine

WORKDIR /salesapp

COPY docker/requirements.txt /

RUN apk add --no-cache uwsgi uwsgi-python gcc linux-headers build-base

RUN pip install -r /requirements.txt

RUN mkdir /var/run/salesapp && mkdir /var/log/salesapp

COPY salesapp/ /salesapp

CMD uwsgi --plugin python3 --emperor /salesapp/salesapp/uwsgi.ini
