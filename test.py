from elasticsearch import Elasticsearch
import json

es = Elasticsearch("http://localhost:9200")
resp = es.search(index="zeek-ai-anomalies", size=1)
doc = resp["hits"]["hits"][0]["_source"]
print(json.dumps(doc, indent=2, default=str))