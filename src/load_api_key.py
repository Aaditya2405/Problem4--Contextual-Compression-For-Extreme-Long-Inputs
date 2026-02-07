import os
from pathlib import Path

def load_api_key():
    # 1. Try Environment Variable first
    env_key = os.getenv("GEMINI_API_KEY")
    if env_key:
        return env_key

    # 2. Path relative to THIS file (src/load_api_key.py)
    # .parent is 'src', .parent.parent is the root 'Explainable-QA-Hackathon'
    base_dir = Path(__file__).resolve().parent.parent
    
    # NOTE: Your screenshot shows the folder is named 'secret' (singular)
    key_path = base_dir / "secret" / "gemini_api_key.txt"
    
    if key_path.exists():
        with open(key_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    # 3. Fallback: Check if we are running from root and 'secret' is right here
    fallback_path = Path.cwd() / "secret" / "gemini_api_key.txt"
    if fallback_path.exists():
        with open(fallback_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    raise RuntimeError(f"API Key not found! Checked: {key_path}")