import pandas as pd
import os

INPUT_FILE = "content_metadata.csv"
OUTPUT_FILE = "annotated_results.csv"

def main():
    print("--- 📝 SETTING UP LOCAL AI ANNOTATION SHEET ---")
    if not os.path.exists(INPUT_FILE): return
    
    df = pd.read_csv(INPUT_FILE)
    output_df = pd.DataFrame()
    output_df['Tool Name'] = df.get('tool_name', df.get('Tool Name'))
    output_df['URL'] = df.get('extracted_url', df.get('url'))
    
    output_df['Abdullah_Annotation'] = "" 
    output_df['Abdullah_Notes'] = ""
    output_df['LLM_Decision'] = ""
    output_df['LLM_Reasoning'] = ""
    output_df['content_file'] = df['content_file']

    output_df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Created '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()