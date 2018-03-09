FROM python:3.6-alpine
RUN mkdir -p project \
    && apk add --no-cache musl-dev python3-dev postgresql-dev gcc \
    && python -m pip install --no-cache-dir pipenv django psycopg2 \
    && rm -rf /var/cache/apk/*
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]