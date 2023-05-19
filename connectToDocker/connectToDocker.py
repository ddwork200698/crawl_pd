from elasticsearch import Elasticsearch
es = Elasticsearch(['http://localhost:9200']) # connecting to elasticsearch
print(es.ping())
