# FILE: src/generators/sbom_generator.py
import json

def generate_sbom(spec, output_path):
    sbom = {
        "spec_version": "v2.0",
        "components": [
            {"name": "mapper", "version": "1.0"},
            {"name": "sbom_generator", "version": "1.0"},
        ],
        "metadata": {"created": "2025-10-05"},
    }
    with open(output_path, "w") as f:
        json.dump(sbom, f, indent=2)
