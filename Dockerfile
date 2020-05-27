FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl python3-pip python3-wheel supervisor \
    && pip3 install -U pip setuptools \
    && pip install flask gunicorn[gevent]==20.0.0 requests

COPY app/ /usr/app/
COPY config/ /usr/config/
COPY bin/ /usr/bin/

RUN chmod +x /usr/bin/statuser.py

WORKDIR /usr/app

CMD ["/usr/bin/supervisord", "-c", "/usr/config/supervisord.conf"]


