# FILE: cli/specforge.py
import typer, yaml
from src.core.mapper import map_idea_to_spec, save_spec
from src.generators.sbom_generator import generate_sbom
from src.generators.patent_scaffold import create_patent_scaffold

app = typer.Typer()

@app.command()
def map(idea: str, out: str = "dist/example_outputs/SPEC.yaml", seed: int = 42):
    spec = map_idea_to_spec(idea, seed)
    save_spec(spec, out)
    typer.echo(f"SPEC generated → {out}")

@app.command()
def sbom(spec_path: str, out: str = "dist/example_outputs/SBOM.json"):
    spec = yaml.safe_load(open(spec_path))
    generate_sbom(spec, out)
    typer.echo(f"SBOM generated → {out}")

@app.command()
def patent(spec_path: str, out: str = "dist/example_outputs/PATENT_DRAFT.md"):
    spec = yaml.safe_load(open(spec_path))
    create_patent_scaffold(spec, out)
    typer.echo(f"Patent scaffold → {out}")

if __name__ == "__main__":
    app()
