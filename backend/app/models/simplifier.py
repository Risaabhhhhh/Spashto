import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from ..config import settings
from functools import lru_cache

# We use global variables to ensure model is loaded once
_model = None
_tokenizer = None

def load_model():
    global _model, _tokenizer
    if _model is None:
        print(f"Loading simplifier model: {settings.MODEL_NAME}")
        _tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
        _model = AutoModelForSeq2SeqLM.from_pretrained(settings.MODEL_NAME)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        _model = _model.to(device)

@lru_cache(maxsize=100)
def simplify_text(text: str, target_lang: str) -> str:
    if _model is None:
        load_model()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # For zero-shot, prompt appropriately
    prompt = f"Simplify the following text into plain {target_lang}:\n{text}"
    inputs = _tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).to(device)
    
    with torch.no_grad():
        outputs = _model.generate(**inputs, max_length=256)
    
    generated_text = _tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text
