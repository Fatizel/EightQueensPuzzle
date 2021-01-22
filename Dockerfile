FROM postgres:latest

RUN apt -q update \
    && apt -q dist-upgrade \
    && apt install -yq python3 python3-psycopg2 python-sqlalchemy python-pytest \
    && ln -s /usr/lib/python2.7/dist-packages /usr/lib/python3.7 \
    && mkdir -p /opt/queen  \
    && chown postgres:postgres /opt/queen 

COPY python/* /opt/queen/

USER postgres:postgres

WORKDIR /opt/queen/


