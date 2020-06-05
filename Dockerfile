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


# to build (here against the jargon test framework) and also requires the docker-compose elements for running elastic search
# for the docker-compose elastic search framework see https://github.com/angrygoat/metadata-and-file-props-indexer/tree/master/docker-framework

# docker build -t grid-search-service .

# docker run --name grid-search-service -v `pwd`/etc/irods-ext:/etc/irods-ext -p 8082:8082 --network="4-2_irodsnet" grid-search-service

