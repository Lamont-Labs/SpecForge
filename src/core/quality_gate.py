# FILE: src/core/quality_gate.py
def validate_quality(text: str) -> bool:
    banned = ["TBD", "LOREM", "PLACEHOLDER"]
    return not any(b in text for b in banned)
