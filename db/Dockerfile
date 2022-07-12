FROM postgres:latest

ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=diversify_db

COPY /db/sql/initdb.sql /docker-entrypoint-initdb.d/

EXPOSE 5432