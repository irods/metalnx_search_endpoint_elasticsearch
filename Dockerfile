FROM python:3-alpine

RUN apk add build-base
RUN apk add libffi-dev
RUN apk add libressl-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install connexion[swagger-ui]

COPY . /usr/src/app

ENV SEARCH_PROPERTIES_FILE=/etc/irods-ext/project-and-sample-search.properties

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]