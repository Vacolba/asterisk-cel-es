FROM python:3-slim

RUN echo Europe/Madrid | tee /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

ADD . /app

WORKDIR /app

RUN pip install requests

VOLUME /data
VOLUME /etc/ssl/certs
VOLUME /tmp

ENTRYPOINT ["./app.sh"]
