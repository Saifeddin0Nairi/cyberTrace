from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch("http://localhost:9200")

reponse = es.search(
    index="zeek-*",
    body={
        "size": 10000,
        "query": {"term": {"log_type": "conn"}},
        "_source": [
            "id.orig_h", "id.resp_h", "id.orig_p", "id.resp_p",
            "proto", "duration", "orig_bytes", "resp_bytes",
            "orig_pkts", "resp_pkts", "conn_state", "missed_bytes"
        ]
    }
)

lignes = [h["_source"] for h in reponse["hits"]["hits"]]
df = pd.DataFrame(lignes)
df.to_csv("C:\\elk\\zeek_logs_export.csv", index=False)
print(f"✅ Export terminé : {len(df)} lignes → zeek_logs_export.csv")