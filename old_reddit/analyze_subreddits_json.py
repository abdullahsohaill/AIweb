import json
import pandas as pd
from pathlib import Path

# --- Load file ---
path = Path("out/subreddits_metadata.json")
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Normalize to DataFrame ---
df = pd.json_normalize(data)

# Keep only numeric columns of interest
cols = ["subreddit", "subscribers", "avg_posts_per_day", "recent_post_count", "recent_comment_count"]
df = df[cols]

# --- Basic descriptive stats ---
total = len(df)
gt_10k = (df["subscribers"] > 10_000).sum()
gt_100k = (df["subscribers"] > 100_000).sum()
gt_1m = (df["subscribers"] > 1_000_000).sum()
gt_1_post_day = (df["avg_posts_per_day"] > 1).sum()
avg_subs = df["subscribers"].mean()
median_subs = df["subscribers"].median()
avg_posts = df["avg_posts_per_day"].mean()
corr = df[["subscribers", "avg_posts_per_day"]].corr().iloc[0, 1]

# --- Print summary ---
print("\n=== BASIC SUBREDDIT STATS ===")
print(f"Total subreddits crawled: {total}")
print(f"> 10K subscribers: {gt_10k}")
print(f"> 100K subscribers: {gt_100k}")
print(f"> 1M subscribers: {gt_1m}")
print(f"> 1 post/day avg: {gt_1_post_day}")
print()
print(f"Average subscribers: {avg_subs:,.0f}")
print(f"Median subscribers:  {median_subs:,.0f}")
print(f"Average posts/day:   {avg_posts:.2f}")
print(f"Corr(subs, posts/day): {corr:.2f}")
# print("\nTop 80 by subscribers:")
# print(df.sort_values("subscribers", ascending=False).head(40)[["subreddit", "subscribers", "avg_posts_per_day"]])
# print(df.sort_values("subscribers", ascending=False).tail(40)[["subreddit", "subscribers", "avg_posts_per_day"]])


# --- NEW: Filtered view for >=100K subscribers ---
print("\n=== SUBREDDITS WITH ≥100K MEMBERS ===")
top_df = df[df["subscribers"] >= 100_000].sort_values("subscribers", ascending=False)
print(top_df[["subreddit", "subscribers", "avg_posts_per_day", "recent_post_count", "recent_comment_count"]].head(40))
print(top_df[["subreddit", "subscribers", "avg_posts_per_day", "recent_post_count", "recent_comment_count"]].tail(40))


print(f"\nTotal with ≥100K members: {(top_df)}")