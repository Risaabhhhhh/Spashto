import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import sys
import os
from tqdm import tqdm

# Add parent directory to path to import evaluation scripts
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from evaluation.semantic_preservation import evaluate_semantic_preservation

def run_baseline_eval():
    test_path = "dataset/splits/test.csv"
    if not os.path.exists(test_path):
        print(f"File {test_path} not found. Run dataset/split_by_document.py first.")
        return

    df = pd.read_csv(test_path)
    if len(df) == 0:
        print("Test set is empty. Cannot evaluate.")
        return

    # Using mT5-small as the selected multilingual model for the zero-shot baseline
    model_name = "google/mt5-small"
    print(f"Loading model {model_name} for zero-shot baseline...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    predictions = []
    references = df['simplified_text'].tolist()
    sources = df['original_text'].tolist()

    print(f"Generating zero-shot simplifications for {len(sources)} test segments...")
    for source in tqdm(sources):
        # Prompt for simplification (zero-shot)
        prompt = f"Simplify the following legal text into plain English:\n{source}"
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).to(device)
        
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=256)
        
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        predictions.append(generated_text)
    
    print("\nRunning Semantic Preservation Evaluation (BERTScore)...")
    results = evaluate_semantic_preservation(predictions, references, lang="en")
    
    print("\n" + "="*50)
    print("--- Baseline Results (Zero-Shot mT5) ---")
    print("="*50)
    print(f"Dataset Size Evaluated : {len(df)} segments")
    print(f"Semantic Preservation (BERTScore F1) : {results['f1']:.4f}")
    print(f"Precision : {results['precision']:.4f}")
    print(f"Recall    : {results['recall']:.4f}")
    print("="*50)
    
    # Show examples
    print("\nExamples:")
    for i in range(min(2, len(sources))):
        print(f"\n[Example {i+1}]")
        print(f"Original Text   : {sources[i]}")
        print(f"Reference       : {references[i]}")
        print(f"Predicted       : {predictions[i]}")

if __name__ == "__main__":
    run_baseline_eval()
