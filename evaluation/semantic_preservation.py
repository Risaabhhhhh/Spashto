from bert_score import score

def evaluate_semantic_preservation(candidates, references, lang="en"):
    """
    Evaluates semantic similarity between generated candidates and references using BERTScore.
    """
    # Disable verbose logging and use a lightweight model by default to prevent large downloads for baseline
    P, R, F1 = score(candidates, references, lang=lang, verbose=False, model_type="distilbert-base-uncased")
    
    return {
        "precision": P.mean().item(),
        "recall": R.mean().item(),
        "f1": F1.mean().item()
    }
