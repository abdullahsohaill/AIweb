import pandas as pd
import os
from sklearn.metrics import cohen_kappa_score, accuracy_score, confusion_matrix

# --- CONFIGURATION ---
INPUT_FILE = "annotated_results.csv"

def main():
    print("--- 📊 INTER-ANNOTATOR RELIABILITY CHECKER ---")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file '{INPUT_FILE}' not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    
    # Normalize columns just to be safe
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Check required columns
    if 'abdullah_annotation' not in df.columns or 'llm_decision' not in df.columns:
        print(f"❌ Error: Columns not found. Available columns: {list(df.columns)}")
        return

    # Filter for rows where YOU provided an annotation (ignore empty ones)
    # We allow '1', '0', 1, 0, 1.0, 0.0
    df_graded = df.dropna(subset=['abdullah_annotation']).copy()
    
    # Convert to integer for comparison
    try:
        df_graded['abdullah_annotation'] = df_graded['abdullah_annotation'].astype(int)
        df_graded['llm_decision'] = df_graded['llm_decision'].fillna(0).astype(int)
    except ValueError:
        print("❌ Error: Annotations must be numbers (1 or 0). Please check your CSV for text in the annotation columns.")
        return
    
    if len(df_graded) == 0:
        print("⚠️  No manual annotations found. Please fill column 'abdullah_annotation' in the CSV first.")
        return

    y_human = df_graded['abdullah_annotation']
    y_llm = df_graded['llm_decision']
    
    print(f"\nComparing {len(df_graded)} samples...")
    
    # 1. Accuracy (Raw Agreement)
    acc = accuracy_score(y_human, y_llm)
    print(f"✅ Raw Accuracy:       {acc:.2%}")
    
    # 2. Cohen's Kappa (The Research Standard)
    kappa = cohen_kappa_score(y_human, y_llm)
    print(f"🤝 Cohen's Kappa:      {kappa:.4f}")
    
    # Interpretation
    if kappa < 0: interp = "Poor (Worse than chance)"
    elif kappa <= 0.20: interp = "Slight"
    elif kappa <= 0.40: interp = "Fair"
    elif kappa <= 0.60: interp = "Moderate"
    elif kappa <= 0.80: interp = "Substantial"
    else: interp = "Perfect / Almost Perfect"
    
    print(f"   -> Interpretation: {interp}")

    # 3. Confusion Matrix
    # Labels: [0, 1] -> TN, FP, FN, TP
    try:
        tn, fp, fn, tp = confusion_matrix(y_human, y_llm, labels=[0, 1]).ravel()
        print(f"\n--- 🔍 Detailed Breakdown ---")
        print(f"Match - True Negatives (Both say 0):     {tn}")
        print(f"Match - True Positives (Both say 1):     {tp}")
        print(f"Mismatch - False Positives (LLM=1, You=0): {fp}  <-- LLM too lenient?")
        print(f"Mismatch - False Negatives (LLM=0, You=1): {fn}  <-- LLM too strict?")
        
        # 4. Show Disagreements
        if fp > 0 or fn > 0:
            print(f"\n--- 📝 Disagreements (Check these rows) ---")
            mismatches = df_graded[df_graded['abdullah_annotation'] != df_graded['llm_decision']]
            for i, row in mismatches.iterrows():
                print(f"Row {i}: {row.get('tool_name', 'Unknown')} (URL: {row.get('url', 'Unknown')})")
                print(f"   You: {row['abdullah_annotation']} | LLM: {row['llm_decision']}")
                print(f"   LLM Reason: {row.get('llm_reasoning', 'N/A')[:100]}...")
                print("-" * 40)
    except Exception as e:
        print(f"Could not generate confusion matrix (possibly only one class present): {e}")

if __name__ == "__main__":
    main()