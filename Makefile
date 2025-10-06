# FILE: Makefile
APP=specforge
VERSION=v2.0

demo:
	@echo "Running SpecForge demo..."
	python cli/specforge.py map examples/idea.txt --out dist/example_outputs/SPEC.yaml --seed 42
	python cli/specforge.py sbom dist/example_outputs/SPEC.yaml --out dist/example_outputs/SBOM.json
	python cli/specforge.py patent dist/example_outputs/SPEC.yaml --out dist/example_outputs/PATENT_DRAFT.md
	bash verify.sh

clean:
	rm -rf dist/example_outputs/* SBOM/checksums.csv

verify:
	bash verify.sh
