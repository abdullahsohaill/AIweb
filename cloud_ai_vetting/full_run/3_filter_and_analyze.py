import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FILE = "full_annotated_results.csv"
OUTPUT_FILE = "final_cloud_ai_web_integrable.csv"

def main():
    print("--- 📊 CLOUD AI: FINAL RESULTS ANALYSIS ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: {INPUT_FILE} not found.")
        return

    # 1. Load Data
    df = pd.read_csv(INPUT_FILE)
    total_rows = len(df)
    
    # Ensure decision column is numeric (handle potential parsing errors)
    df['llm_decision'] = pd.to_numeric(df['llm_decision'], errors='coerce').fillna(0).astype(int)

    # 2. Calculate Statistics
    count_yes = len(df[df['llm_decision'] == 1])
    count_no = len(df[df['llm_decision'] == 0])
    
    # Calculate percentages
    pct_yes = (count_yes / total_rows) * 100 if total_rows > 0 else 0
    pct_no = (count_no / total_rows) * 100 if total_rows > 0 else 0

    print(f"\n📈 Classification Statistics:")
    print(f"   Total Processed:      {total_rows:,}")
    print(f"   -----------------------------------------")
    print(f"   ✅ Web-Integrable (1): {count_yes:,}  ({pct_yes:.1f}%)")
    print(f"   ❌ Consumer Only (0):  {count_no:,}  ({pct_no:.1f}%)")

    # 3. Filter and Save
    print(f"\n💾 Saving Web-Integrable tools to '{OUTPUT_FILE}'...")
    
    # Filter for 1s
    df_final = df[df['llm_decision'] == 1].copy()
    
    # Save
    df_final.to_csv(OUTPUT_FILE, index=False)
    print(f"   ✅ Success! {len(df_final):,} tools saved.")

    # 4. (Optional) Peek at the top reasons
    if len(df_final) > 0:
        print("\n📝 Sample Reasons for 'Yes' (First 3):")
        for i, row in df_final.head(3).iterrows():
            print(f"   - {row.get('tool_name')}: {row.get('llm_reasoning')[:150]}...")

if __name__ == "__main__":
    main()