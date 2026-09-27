import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split_dataset():
    input_path = "dataset/labeled/indian_gov_legal_simplification.csv"
    if not os.path.exists(input_path):
        print(f"File {input_path} not found. Run scraper.py first.")
        return

    df = pd.read_csv(input_path)
    
    # Get unique documents with their type for stratification
    documents = df[['document_id', 'document_type']].drop_duplicates()
    
    # Split documents into train/val/test
    # 60% Train, 20% Val, 20% Test
    try:
        train_docs, temp_docs = train_test_split(
            documents, test_size=0.4, stratify=documents['document_type'], random_state=42
        )
        val_docs, test_docs = train_test_split(
            temp_docs, test_size=0.5, stratify=temp_docs['document_type'], random_state=42
        )
    except ValueError:
        # Fallback if not enough samples in each class to stratify
        train_docs, temp_docs = train_test_split(
            documents, test_size=0.4, random_state=42
        )
        val_docs, test_docs = train_test_split(
            temp_docs, test_size=0.5, random_state=42
        )
        
    # Map back to original segments
    train_df = df[df['document_id'].isin(train_docs['document_id'])]
    val_df = df[df['document_id'].isin(val_docs['document_id'])]
    test_df = df[df['document_id'].isin(test_docs['document_id'])]
    
    os.makedirs("dataset/splits", exist_ok=True)
    train_df.to_csv("dataset/splits/train.csv", index=False)
    val_df.to_csv("dataset/splits/val.csv", index=False)
    test_df.to_csv("dataset/splits/test.csv", index=False)
    
    print(f"Splits created successfully:")
    print(f"Train: {len(train_df)} segments ({len(train_docs)} documents)")
    print(f"Val: {len(val_df)} segments ({len(val_docs)} documents)")
    print(f"Test: {len(test_df)} segments ({len(test_docs)} documents)")

if __name__ == "__main__":
    split_dataset()
