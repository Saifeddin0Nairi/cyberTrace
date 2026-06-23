from elasticsearch import Elasticsearch
import pandas as pd
from datetime import datetime
import numpy as np

es = Elasticsearch("http://localhost:9200")
df = pd.read_csv("C:\\elk\\resultats_ia.csv").fillna(0)

try:
    es.indices.delete(index="zeek-ai-anomalies", ignore_unavailable=True)
except:
    pass

compteur = 0
for _, row in df.iterrows():
    doc = row.to_dict()
    for k, v in doc.items():
        if isinstance(v, np.integer): doc[k] = int(v)
        elif isinstance(v, np.floating): doc[k] = float(v)
    doc["@timestamp"] = datetime.utcnow().isoformat()
    es.index(index="zeek-ai-anomalies", document=doc)
    compteur += 1

print(f"✅ {compteur} documents injectés dans zeek-ai-anomalies")