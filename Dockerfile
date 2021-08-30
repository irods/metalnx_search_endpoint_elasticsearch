FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apt update
RUN apt install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

#RUN python3 -m pip install connexion[swagger-ui]

COPY . /usr/src/app

ENV SEARCH_PROPERTIES_FILE=/etc/irods-ext/project-and-sample-search.properties

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]


# to build (here against the jargon test framework) and also requires the docker-compose elements for running elastic search
# for the docker-compose elastic search framework see https://github.com/angrygoat/metadata-and-file-props-indexer/tree/master/docker-framework

# docker build -t grid-search-service .

# docker run --name grid-search-service -v `pwd`/etc/irods-ext:/etc/irods-ext -p 8082:8082 --network="4-2_irodsnet" grid-search-service

