import hashlib

def generate_text_hash(text: str) -> str:
    """Generate a hash for a given text to be used in caching."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
