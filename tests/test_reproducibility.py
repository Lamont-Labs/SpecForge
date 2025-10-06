# FILE: tests/test_reproducibility.py
from src.core.mapper import map_idea_to_spec

def test_determinism():
    spec1 = map_idea_to_spec("solar charger", 42)
    spec2 = map_idea_to_spec("solar charger", 42)
    assert spec1["IdeaHash"] == spec2["IdeaHash"]
