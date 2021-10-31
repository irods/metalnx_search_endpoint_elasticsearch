# Metalnx Search Endpoint for ElasticSearch

## Configuration

Copy and edit the sample configuration:
```
cp server.properties.template server.properties
```

```
es.baseurl=http://localhost:9200
jwt.issuer=issuer
jwt.secret=secretsecretsecretsecretsecretsecretsecretsecret
jwt.lifetime.seconds=600
jwt.algo=HS384
project.url.prefix=deprecated
```

The `es.baseurl` should point to the ElasticSearch holding the indices of interest.

The `jwt` information, most importantly the `jwt.secret` value, must match the settings in `metalnx.properties` in the connected Metalnx application.

## Running with Docker

```bash
# build the image
docker build -t myimages/metalnx_search_elasticsearch .

# start the container
docker run -p 8082:8082 $(pwd)/server.properties:/etc/irods-ext/project-and-sample-search.properties myimages/metalnx_search_elasticsearch
```

The endpoint will be available at http://localhost:8082/v1
