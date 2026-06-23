# generate_ndjson.py
import json
import os

# Définition de l'index pattern (data view)
data_view = {
    "type": "index-pattern",
    "id": "zeek-ai-anomalies",
    "attributes": {
        "title": "zeek-ai-anomalies",
        "timeFieldName": "@timestamp"
    },
    "references": []
}

# Visualisation 1 : Compteur d'anomalies
vis_count = {
    "type": "visualization",
    "id": "vis-anomalies-count",
    "attributes": {
        "title": "Nombre total d'anomalies",
        "visState": json.dumps({
            "type": "metric",
            "params": {"metric": {"percentageMode": False}},
            "aggs": [
                {"id": "1", "type": "count", "schema": "metric", "params": {}},
                {"id": "2", "type": "filters", "schema": "bucket",
                 "params": {"filters": [{"input": {"query": "ai_anomalie:true"}}]}}
            ]
        }),
        "uiStateJSON": "{}",
        "description": "",
        "version": 1,
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({
                "index": "zeek-ai-anomalies",
                "query": {"match_all": {}},
                "filter": []
            })
        }
    },
    "references": [{"id": "zeek-ai-anomalies", "name": "index-pattern", "type": "index-pattern"}]
}

# Visualisation 2 : Score IA moyen
vis_avg = {
    "type": "visualization",
    "id": "vis-avg-score",
    "attributes": {
        "title": "Score IA moyen (anomalies)",
        "visState": json.dumps({
            "type": "metric",
            "params": {"metric": {"percentageMode": False}},
            "aggs": [
                {"id": "1", "type": "avg", "schema": "metric", "params": {"field": "ai_score"}},
                {"id": "2", "type": "filters", "schema": "bucket",
                 "params": {"filters": [{"input": {"query": "ai_anomalie:true"}}]}}
            ]
        }),
        "uiStateJSON": "{}",
        "description": "",
        "version": 1,
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({
                "index": "zeek-ai-anomalies",
                "query": {"match_all": {}},
                "filter": []
            })
        }
    },
    "references": [{"id": "zeek-ai-anomalies", "name": "index-pattern", "type": "index-pattern"}]
}

# Visualisation 3 : Timeline des anomalies
vis_timeline = {
    "type": "visualization",
    "id": "vis-timeline",
    "attributes": {
        "title": "Anomalies dans le temps",
        "visState": json.dumps({
            "type": "line",
            "params": {"addLegend": True},
            "aggs": [
                {"id": "1", "type": "count", "schema": "metric", "params": {}},
                {"id": "2", "type": "date_histogram", "schema": "segment",
                 "params": {"field": "@timestamp", "interval": "auto"}},
                {"id": "3", "type": "filters", "schema": "group",
                 "params": {"filters": [{"input": {"query": "ai_anomalie:true"}}]}}
            ]
        }),
        "uiStateJSON": "{}",
        "description": "",
        "version": 1,
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({
                "index": "zeek-ai-anomalies",
                "query": {"match_all": {}},
                "filter": []
            })
        }
    },
    "references": [{"id": "zeek-ai-anomalies", "name": "index-pattern", "type": "index-pattern"}]
}

# Visualisation 4 : Top 10 IPs sources
vis_top_ips = {
    "type": "visualization",
    "id": "vis-top-ips",
    "attributes": {
        "title": "Top 10 IPs sources suspectes",
        "visState": json.dumps({
            "type": "table",
            "params": {"perPage": 10},
            "aggs": [
                {"id": "1", "type": "count", "schema": "metric", "params": {}},
                {"id": "2", "type": "terms", "schema": "bucket",
                 "params": {"field": "id.orig_h", "size": 10, "order": "desc"}},
                {"id": "3", "type": "filters", "schema": "bucket",
                 "params": {"filters": [{"input": {"query": "ai_anomalie:true"}}]}}
            ]
        }),
        "uiStateJSON": "{}",
        "description": "",
        "version": 1,
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({
                "index": "zeek-ai-anomalies",
                "query": {"match_all": {}},
                "filter": []
            })
        }
    },
    "references": [{"id": "zeek-ai-anomalies", "name": "index-pattern", "type": "index-pattern"}]
}

# Visualisation 5 : Répartition des états de connexion (camembert)
vis_conn_state = {
    "type": "visualization",
    "id": "vis-conn-state-pie",
    "attributes": {
        "title": "États de connexion (anomalies)",
        "visState": json.dumps({
            "type": "pie",
            "params": {"isDonut": True, "addLegend": True},
            "aggs": [
                {"id": "1", "type": "count", "schema": "metric", "params": {}},
                {"id": "2", "type": "terms", "schema": "segment",
                 "params": {"field": "conn_state", "size": 10}},
                {"id": "3", "type": "filters", "schema": "segment",
                 "params": {"filters": [{"input": {"query": "ai_anomalie:true"}}]}}
            ]
        }),
        "uiStateJSON": "{}",
        "description": "",
        "version": 1,
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({
                "index": "zeek-ai-anomalies",
                "query": {"match_all": {}},
                "filter": []
            })
        }
    },
    "references": [{"id": "zeek-ai-anomalies", "name": "index-pattern", "type": "index-pattern"}]
}

# Visualisation 6 : Histogramme des scores IA
vis_score_hist = {
    "type": "visualization",
    "id": "vis-score-histogram",
    "attributes": {
        "title": "Distribution du score IA (anomalies)",
        "visState": json.dumps({
            "type": "histogram",
            "params": {"addLegend": False},
            "aggs": [
                {"id": "1", "type": "count", "schema": "metric", "params": {}},
                {"id": "2", "type": "histogram", "schema": "segment",
                 "params": {"field": "ai_score", "interval": 0.05, "extended_bounds": {"min": 0, "max": 1}}},
                {"id": "3", "type": "filters", "schema": "bucket",
                 "params": {"filters": [{"input": {"query": "ai_anomalie:true"}}]}}
            ]
        }),
        "uiStateJSON": "{}",
        "description": "",
        "version": 1,
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({
                "index": "zeek-ai-anomalies",
                "query": {"match_all": {}},
                "filter": []
            })
        }
    },
    "references": [{"id": "zeek-ai-anomalies", "name": "index-pattern", "type": "index-pattern"}]
}

# Dashboard final
dashboard = {
    "type": "dashboard",
    "id": "cybertrace-dashboard-final",
    "attributes": {
        "title": "CyberTrace — Monitoring Réseau IA",
        "description": "Tableau de bord des anomalies détectées par RandomForest",
        "panelsJSON": json.dumps([
            {"panelIndex": "1", "gridData": {"x":0, "y":0, "w":12, "h":6, "i":"1"}, "type": "visualization", "id": "vis-anomalies-count"},
            {"panelIndex": "2", "gridData": {"x":12, "y":0, "w":12, "h":6, "i":"2"}, "type": "visualization", "id": "vis-avg-score"},
            {"panelIndex": "3", "gridData": {"x":0, "y":6, "w":24, "h":7, "i":"3"}, "type": "visualization", "id": "vis-timeline"},
            {"panelIndex": "4", "gridData": {"x":24, "y":6, "w":12, "h":7, "i":"4"}, "type": "visualization", "id": "vis-conn-state-pie"},
            {"panelIndex": "5", "gridData": {"x":0, "y":13, "w":18, "h":8, "i":"5"}, "type": "visualization", "id": "vis-top-ips"},
            {"panelIndex": "6", "gridData": {"x":18, "y":13, "w":18, "h":8, "i":"6"}, "type": "visualization", "id": "vis-score-histogram"}
        ]),
        "optionsJSON": json.dumps({"useMargins": True}),
        "version": 1,
        "timeRestore": False,
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({"query": {"match_all": {}}, "filter": []})
        }
    },
    "references": [
        {"id": "vis-anomalies-count", "name": "1:panel_1", "type": "visualization"},
        {"id": "vis-avg-score", "name": "1:panel_2", "type": "visualization"},
        {"id": "vis-timeline", "name": "1:panel_3", "type": "visualization"},
        {"id": "vis-conn-state-pie", "name": "1:panel_4", "type": "visualization"},
        {"id": "vis-top-ips", "name": "1:panel_5", "type": "visualization"},
        {"id": "vis-score-histogram", "name": "1:panel_6", "type": "visualization"},
        {"id": "zeek-ai-anomalies", "name": "2:index-pattern", "type": "index-pattern"}
    ]
}

# Écrire le fichier ndjson
output_file = "cybertrace_dashboard.ndjson"
with open(output_file, "w", encoding="utf-8") as f:
    for obj in [data_view, vis_count, vis_avg, vis_timeline, vis_top_ips, vis_conn_state, vis_score_hist, dashboard]:
        f.write(json.dumps(obj) + "\n")

print(f"✅ Fichier généré : {output_file}")
print("Importez-le dans Kibana : Stack Management → Saved Objects → Import")