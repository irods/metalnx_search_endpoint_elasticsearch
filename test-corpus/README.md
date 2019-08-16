# Initiating Elastic Search

## Uses elastic search docker(V 7.3.0) container:
``` docker
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --rm --name ES docker.elastic.co/elasticsearch/elasticsearch:7.3.0
```

## Load create dummy indexes and add test index JSONs
```
python3 grid-search-service/test-corpus/load_data.py \
-b "http://localhost:9200" \
-p "grid-search-service/test-corpus/project_jsons" \
-s "grid-search-service/test-corpus/sample_jsons" \
-m "grid-search-service/test-corpus/index_mapping
```