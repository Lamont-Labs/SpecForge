# FILE: src/core/provenance.py
import hashlib, json, time

def record_provenance(file_paths, output_file="SBOM/checksums.csv"):
    """Create a checksum manifest for reproducibility."""
    with open(output_file, "w") as f:
        for path in file_paths:
            h = hashlib.sha256(open(path, "rb").read()).hexdigest()
            f.write(f"{h},{path}\n")

    with open("SBOM/provenance.json", "w") as pf:
        pf.write(json.dumps({"generated": time.time(), "files": len(file_paths)}, indent=2))
