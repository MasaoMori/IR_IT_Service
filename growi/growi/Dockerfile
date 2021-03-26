FROM weseek/growi:4.2.8

ENV APP_DIR /opt/growi

# install dockerize
ENV DOCKERIZE_VERSION v0.6.1
USER root
RUN apk add --no-cache --virtual .dl-deps curl \
    && curl -sL https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
        | tar -xz -C /usr/local/bin \
    && apk del .dl-deps

WORKDIR ${APP_DIR}
