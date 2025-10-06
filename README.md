# FILE: README.md
# SpecForge™ — Deterministic Invention Mapping with SBOMs and Attorney-Ready Handoffs
Version: v2.0 • Date: 2025-10-05 • Owner: Jesse J. Lamont

SpecForge™ converts invention ideas into reproducible SPECs, SBOMs, and provisional-style patent scaffolds.
This repository is a **demo-only**, fully deterministic showcase with provenance, reproducibility proof, and handoff packaging.

## Highlights
- Deterministic mapping (idea → SPEC.yaml)
- SBOM + provenance bundle
- Attorney-ready draft scaffold (non-binding)
- `verify.sh` reproducibility check

## Quickstart
See [docs/QUICKSTART.md](docs/QUICKSTART.md)

## Key Paths
- `/src/core/`: main mapping + validation
- `/src/generators/`: SBOM and patent scaffolds
- `/cli/`: entrypoint via Typer CLI
- `/tests/`: reproducibility and quality validation
- `/SBOM/`: generated software bill of materials
- `/dist/`: example golden outputs

## License
MIT-style demo license © 2025 Jesse J. Lamont
