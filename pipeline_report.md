===========================================================
          AI TOOLS DATA PIPELINE REPORT
===========================================================

PHASE 1: MARKETPLACE AGGREGATION (aggregator1.py)
-----------------------------------------------------------
Input: 37+ Marketplace Crawlers
- Total Raw Rows Loaded:       99,917
- Rows After Link Cleaning:    91,730
- Duplicate URLs Removed:      28,400
-----------------------------------------------------------
=> OUTPUT: 63,330 Unique Marketplace URLs
   (File: DEDUPLICATED_AI_TOOLS_MASTER.csv)


PHASE 2: MERGE, CLEAN & RANKING (aggregator2.py)
-----------------------------------------------------------
Input: Marketplace Master + General Crawlers (Reddit/Google/GitHub)
*Includes URL parameter stripping (utm_source, ref, etc.)*

- Total Candidates to Rank:     69,336 (Unique Cleaned URLs)
- Unranked Tools (Cut):         19,355 (27.9%)
- Ranked Tools (Kept):          49,981 (72.1%)

Ranking Breakdown:
- Top 1 Million:                30,805 (61.6%)
- Top 5 Million:                40,407 (80.8%)
- Top 10 Million:               45,783 (91.6%)
-----------------------------------------------------------
=> OUTPUT: 30,805 High-Traffic Tools (Top 1M)
   (File: final_tools_1M.csv)


PHASE 3: FINAL VETTING (exact_match_cleaner.py)
-----------------------------------------------------------
Input: Top 1M Ranked Tools
- Initial Entries:              30,805
- Blocklist Size:               2,647 domains
- Noise/Irrelevant Removed:     14,629
-----------------------------------------------------------
=> FINAL GOLD DATASET: 16,176 Tools
   (File: final_tools_1M_cleaned.csv)

===========================================================
TOTAL FUNNEL SUMMARY
- Starting Raw Rows:           ~137,000+ (Marketplace + General)
- Final Vetted AI Tools:        16,176
===========================================================