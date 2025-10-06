# FILE: tests/test_quality_gate.py
from src.core.quality_gate import validate_quality

def test_no_placeholders():
    assert validate_quality("Valid idea text") is True
    assert validate_quality("Contains TBD") is False
