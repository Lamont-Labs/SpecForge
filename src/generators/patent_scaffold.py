# FILE: src/generators/patent_scaffold.py
def create_patent_scaffold(spec, output_path):
    with open(output_path, "w") as f:
        f.write("# PROVISIONAL PATENT DRAFT\n")
        f.write("## Title\nDeterministic AI Invention Mapper\n\n")
        f.write("## Claims\n")
        f.write("1. A method for mapping ideas deterministically.\n")
        f.write("2. The method of claim 1 with provenance logging.\n")
