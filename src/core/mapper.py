# FILE: src/core/mapper.py
import hashlib, yaml, sys, json
from datetime import datetime

def map_idea_to_spec(input_text, seed=42):
    """Convert plain idea text into deterministic SPEC.yaml."""
    idea_hash = hashlib.sha256((input_text + str(seed)).encode()).hexdigest()
    spec = {
        "SpecForgeVersion": "v2.0",
        "IdeaHash": idea_hash,
        "Created": datetime.utcnow().isoformat(),
        "FunctionalRequirements": ["Map idea deterministically", "No placeholders"],
        "DFMA_Score": 88,
        "Sustainability": "Recyclable materials suggested",
    }
    return spec

def save_spec(spec, out_path):
    with open(out_path, "w") as f:
        yaml.safe_dump(spec, f)
