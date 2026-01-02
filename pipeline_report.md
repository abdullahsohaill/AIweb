===========================================================
          AI TOOLS DATA PIPELINE REPORT
===========================================================

PHASE 1: MARKETPLACE AGGREGATION (aggregator1.py)
-----------------------------------------------------------
Input: 37+ Marketplace Crawlers
- Total Raw Rows Loaded:       100,116
- Rows After Link Cleaning:     91,929
- Duplicate URLs Removed:       28,403
-----------------------------------------------------------
=> OUTPUT: 63,526 Unique Marketplace URLs
   (File: DEDUPLICATED_AI_TOOLS_MASTER.csv)


PHASE 2: MERGE & RANKING (aggregator2.py)
-----------------------------------------------------------
Input: Marketplace Master + General Crawlers (Reddit/Google/GitHub)
- Total Merged Candidates:      86,400 (Unique URLs)
- Unranked Tools (Cut):         23,314 (27.0%)
- Ranked Tools (Kept):          63,086 (73.0%)

Ranking Breakdown:
- Top 1 Million:                38,857 (61.6%)
- Top 5 Million:                50,999
- Top 10 Million:               57,908
-----------------------------------------------------------
=> OUTPUT: 38,857 High-Traffic Tools (Top 1M)
   (File: final_tools_1M.csv)


PHASE 3: FINAL VETTING (exact_match_cleaner.py)
-----------------------------------------------------------
Input: Top 1M Ranked Tools
- Initial Entries:              38,857
- Blocklist Size:               2,641 domains
- Noise/Irrelevant Removed:     17,007
-----------------------------------------------------------
=> FINAL GOLD DATASET: 21,850 Tools
   (File: final_tools_1M_cleaned.csv)

===========================================================
TOTAL FUNNEL SUMMARY
- Starting Raw Candidates:     ~137,000+ (approx combined raw inputs)
- Final Vetted AI Tools:        21,850
===========================================================