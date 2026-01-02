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

- Total Loaded Tools:           97,506
- Unique Cleaned URLs to Rank:  69,136
- Unranked Tools (Cut):         19,355 (28.0%)
- Ranked Tools (Kept):          49,781 (72.0%)

Ranking Breakdown:
- Top 1 Million:                30,605 (61.5%)
- Top 5 Million:                40,207 (80.8%)
- Top 10 Million:               45,583 (91.6%)
-----------------------------------------------------------
=> OUTPUT: 30,605 High-Traffic Tools (Top 1M)
   (File: final_tools_1M.csv)


PHASE 3: FINAL VETTING (exact_match_cleaner.py)
-----------------------------------------------------------
Input: Top 1M Ranked Tools
- Initial Entries:              30,605
- Blocklist Size:               2,702 domains
- Noise/Irrelevant Removed:     15,614
-----------------------------------------------------------
=> FINAL GOLD DATASET: 15,646 Tools
   (File: final_tools_1M_cleaned.csv)

===========================================================
TOTAL FUNNEL SUMMARY
- Starting Raw Rows:           ~137,000+ (Marketplace + General)
- Final Vetted AI Tools:        14,991
===========================================================