FROM mysql:8.0.23

COPY data/world.sql.gz /docker-entrypoint-initdb.d/

ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
ENV MYSQL_DATABASE=db
ENV MYSQL_USER=root
