# CyberTrace — AI-Assisted Network Forensics

**Automated post-incident network analysis with AI-powered anomaly detection.**

CyberTrace is an end-to-end forensic pipeline that captures network traffic, analyzes it, classifies every connection as *normal* or *anomalous* using machine learning, and visualizes the results in an interactive dashboard — turning raw packet captures into actionable security insight for SOC analysts.

> Final-year project (PFA) — EPI Digital School, Sousse · Networks & Cybersecurity · 2025/2026

---

## Key Results

| Metric | Value |
|---|---|
| Model accuracy (NSL-KDD test set) | **97%** |
| False positive rate | ~0.2% (22 / 12,848) |
| Anomalies detected on real captured traffic | **84.7%** (8,472 / 10,000 connections) |
| Kibana dashboard visualizations | 14+ |

---

## What It Does

- **Captures** attack traffic generated in an isolated virtual lab (Kali Linux → Metasploitable 2).
- **Analyzes** PCAP files with **Zeek IDS** to produce structured connection logs.
- **Ingests & indexes** logs into **Elasticsearch** via **Logstash**.
- **Classifies** each connection (normal vs. anomaly) with a **Random Forest** model trained on the public **NSL-KDD** dataset.
- **Visualizes** the network security posture in an interactive **Kibana** dashboard.
- **Reports** detected incidents automatically, with severity scoring (CRITICAL / HIGH / MEDIUM / LOW).

The whole pipeline runs on local infrastructure — no paid cloud services — and is aligned with **NIST SP 800-86** and **MITRE ATT&CK**.

---

## Tech Stack

`Zeek` · `Elasticsearch` · `Logstash` · `Kibana` · `Wireshark` · `Python (scikit-learn)` · `Random Forest` · `NSL-KDD` · `Kali Linux` · `Metasploitable 2` · `VirtualBox` · `n8n`

---

## Architecture

```
[Kali Linux] --attacks--> [Metasploitable 2]      ← Attack plane (isolated host-only network)
        |
        v  (PCAP capture)
[Zeek IDS] -> [Logstash] -> [Elasticsearch] -> [Kibana]   ← Analysis plane (ELK)
        |
        v
[Random Forest model] -> AI classification -> back into Elasticsearch
        |
        v
[Analyst dashboard + HTML incident report]        ← Access plane
```

---

## Repository Structure

| Path | Description |
|---|---|
| `document/` | Full project report (PFA, PDF) |
| `cybertrace_model.pkl` / `cybertrace_scaler.pkl` | Trained Random Forest model + scaler |
| `*_dashboard.ndjson` | Kibana dashboard definitions |
| `zeek_output/` | Structured Zeek logs |
| `capture_totale.pcap` | Captured network traffic |
| `cybertrace_n8n.json` | n8n automation workflow |
| `export_es_to_csv.py` | Export Elasticsearch data to CSV |
| `inject_results.py` | Inject AI predictions back into Elasticsearch |
| `generate_ndjson.py` / `fix_dashboard.py` | Dashboard generation utilities |

---

## Team

- **Nouisser Oumaima**
- **Jbali Amina**
- **Nairi Saif Edin**

---

📄 Full technical report (French) available in [`/document`](./document).
