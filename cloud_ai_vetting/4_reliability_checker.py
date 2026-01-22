import pandas as pd
from sklearn.metrics import cohen_kappa_score, accuracy_score, confusion_matrix

INPUT_FILE = "annotated_results.csv"

def main():
    if not os.path.exists(INPUT_FILE):
        print("File not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    
    # Filter for rows where you actually provided an annotation
    df_graded = df.dropna(subset=['Abdullah_Annotation'])
    
    if len(df_graded) == 0:
        print("No manual annotations found in 'Abdullah_Annotation' column yet.")
        return

    y_gemini = df_graded['gemini_decision'].astype(int)
    y_human = df_graded['Abdullah_Annotation'].astype(int)
    
    print(f"--- 📊 Reliability Report ({len(df_graded)} samples) ---")
    
    # 1. Accuracy (Raw Agreement)
    acc = accuracy_score(y_human, y_gemini)
    print(f"✅ Raw Agreement (Accuracy): {acc:.2%}")
    
    # 2. Cohen's Kappa (Chance-corrected Agreement)
    kappa = cohen_kappa_score(y_human, y_gemini)
    print(f"🤝 Cohen's Kappa:            {kappa:.4f}")
    
    # Interpretation
    if kappa < 0: interp = "Poor"
    elif kappa <= 0.20: interp = "Slight"
    elif kappa <= 0.40: interp = "Fair"
    elif kappa <= 0.60: interp = "Moderate"
    elif kappa <= 0.80: interp = "Substantial"
    else: interp = "Perfect"
    
    print(f"   -> Interpretation: {interp}")

    # 3. Confusion Matrix
    tn, fp, fn, tp = confusion_matrix(y_human, y_gemini).ravel()
    print(f"\n--- Confusion Matrix ---")
    print(f"True Positives (Both Yes): {tp}")
    print(f"True Negatives (Both No):  {tn}")
    print(f"False Positives (Gemini Yes, You No): {fp}")
    print(f"False Negatives (Gemini No, You Yes): {fn}")

if __name__ == "__main__":
    main()