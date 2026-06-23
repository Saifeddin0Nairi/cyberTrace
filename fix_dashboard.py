import requests

KIBANA = "http://localhost:5601"
HEADERS = {"kbn-xsrf": "true", "Content-Type": "application/json"}
BON_ID = "5aced6dd-1ea5-4130-9e4e-f11530c239f2"

VIS_IDS = [
    "vis-01-total-anomalies",
    "vis-02-total-normal", 
    "vis-03-score-moyen",
    "vis-04-timeline",
    "vis-05-proto",
    "vis-06-conn-state",
    "vis-07-top-src-ips",
    "vis-08-top-dst-ports",
    "vis-09-bytes-orig",
    "vis-10-score-distribution",
    "vis-11-top-dst-ips",
    "vis-12-dns-queries",
    "vis-13-service",
    "vis-14-log-types"
]

print("=== Correction Data View ID ===\n")

for vis_id in VIS_IDS:
    # Lire la visualisation
    r = requests.get(f"{KIBANA}/api/saved_objects/visualization/{vis_id}", headers=HEADERS)
    if r.status_code != 200:
        print(f"❌ Non trouvé : {vis_id}")
        continue
    
    data = r.json()
    attrs = data["attributes"]
    
    # Corriger l'ID dans searchSourceJSON
    import json
    search_source = json.loads(attrs["kibanaSavedObjectMeta"]["searchSourceJSON"])
    search_source["index"] = BON_ID
    attrs["kibanaSavedObjectMeta"]["searchSourceJSON"] = json.dumps(search_source)
    
    # Sauvegarder
    r2 = requests.put(
        f"{KIBANA}/api/saved_objects/visualization/{vis_id}",
        headers=HEADERS,
        json={"attributes": attrs}
    )
    
    if r2.status_code == 200:
        print(f"✅ Corrigé : {vis_id}")
    else:
        print(f"❌ Erreur {vis_id} : {r2.status_code} — {r2.text[:100]}")

print("\n=== Terminé ===")
print("Rafraîchis ton dashboard dans Kibana")