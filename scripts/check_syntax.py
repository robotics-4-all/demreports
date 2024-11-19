"""
File that checks the syntax of a demReport file.
"""

from textx import metamodel_from_file

# Load your grammar from a .tx file
meta_model = metamodel_from_file('../grammar/demreport.tx')

# Parse the file to be validated
try:
    model = meta_model.model_from_file('../examples/test.drep')
    print("Syntax is valid!")
except Exception as e:
    print(f"Syntax Error: {e}")
