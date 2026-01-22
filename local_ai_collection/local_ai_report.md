===========================================================
        LOCAL / IN-BROWSER AI DATA PIPELINE REPORT
===========================================================

PHASE 1: DATA COLLECTION (The Crawlers)
-----------------------------------------------------------
Target: Client-side AI, WebGPU, WASM, ONNX, Offline AI
Search Queries: 32 technical phrases

- Google Search Results:        1,783 rows
- Reddit Discussions:           1,254 rows
- GitHub Repositories:          1,211 rows
-----------------------------------------------------------
=> TOTAL RAW INPUTS:            4,248 candidates


PHASE 2: AGGREGATION & RANKING (aggregator_local.py)
-----------------------------------------------------------
- Merged Unique URLs:           3,811
- Successfully Ranked (Tranco): 3,669 (96.2%)
- Unranked (Niche/New):           142 (3.8%)


PHASE 3: CLEANING & VETTING (clean_local_ai.py)
-----------------------------------------------------------
Logic: Strict Blocklist (Noise) + FQDN Deduplication

- Initial Candidates:           3,811
- Noise Blocked:                1,077
  (Top noise: Reddit, Twitter, LinkedIn, Discord)
- Duplicates Merged (FQDN):     1,792
  (Consolidated multiple pages from the same domain)
-----------------------------------------------------------
=> FINAL GOLD DATASET:            942 Unique Local AI Tools
   (File: local_ai_final_cleaned.csv)

===========================================================
SUMMARY
We distilled ~4,200 raw data points down to 942 highly 
specific, unique domains representing Local/Edge AI tools.
===========================================================