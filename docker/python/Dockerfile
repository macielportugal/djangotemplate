FROM python:3.6-alpine
RUN mkdir -p project \
    && apk add --no-cache musl-dev python3-dev postgresql-dev gcc \
    && rm -rf /var/cache/apk/*
WORKDIR /project/app
COPY ./requirements.txt /
RUN python -m pip install --no-cache-dir -r /requirements.txt
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]