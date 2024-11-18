"""
Implements the logic for the model to text transformation.
"""

from textx import metamodel_from_file
from docx import Document

from generation.literals import generate_literals
from generation.parse_model import parse_model
from generation.utilities.add_header import add_header

from generation.introduction.handle_exam import handle_exam
from generation.introduction.handle_patient_info import handle_patient_info
from generation.introduction.handle_tests_list import handle_tests_list
from generation.introduction.handle_scores import handle_scores

from generation.section_1.handle_first_visit import handle_s1_first_visit
from generation.section_1.handle_revisit import handle_s1_revisit
from generation.section_1.handle_last import handle_s1_last

from generation.memory.handle_verbal_memory import handle_verbal_memory
from generation.memory.handle_visual_memory import handle_visual_memory
from generation.memory.handle_conclusions import handle_memory_conclusions

from generation.visuospatial.handle_visuospatial import handle_visuospatial

from generation.executive.handle_executive import handle_executive_functions

from generation.everyday_func.handle_everyday import handle_everyday_functionality

from generation.neuropsy.handle_neuropsy import handle_neuropsychological_symptoms

from generation.outro.conclusions import handle_conclusions
from generation.outro.signature import handle_signature

# Create a new document
document = Document()

# Load the metamodel and model
my_metamodel = metamodel_from_file('../syntax/demreport.tx')
my_model = my_metamodel.model_from_file('../examples/test.drep')
parsed = parse_model(my_model)

lits = generate_literals(parsed)

# Call the functions to handle the parsed data
handle_exam(parsed, document)

add_header(document, "Στοιχεία ασθενή") # ok
handle_patient_info(parsed, document) # ok

add_header(document, "Δοκιμασίες") # ok
handle_tests_list(parsed, document) # ok

add_header(document, "Αποτελέσματα") # ok
handle_scores(parsed, document) # ok

add_header(document, "Εισαγωγή") # ok
handle_s1_first_visit(parsed, document, lits) #οk
handle_s1_revisit(parsed, document, lits) #ok
handle_s1_last(parsed, document, lits) #ok

add_header(document, "Αποτελέσματα νευροψυχολογικής εκτίμησης")
add_header(document, "Μνήμη", 2)
handle_verbal_memory(parsed, document, lits) #ok
handle_visual_memory(parsed, document, lits) #ok
handle_memory_conclusions(parsed, document, lits)

add_header(document, "Οπτικοχωρικές ικανότητες", 2)
handle_visuospatial(parsed, document, lits)

add_header(document, "Εκτελεστικές λειτουργίες", 2)
handle_executive_functions(parsed, document, lits) #needs input from Elena

add_header(document, "Καθημερινή λειτουργικότητα", 2)
handle_everyday_functionality(parsed, document, lits)

add_header(document, "Νευροψυχιατρικά συμπτώματα", 2)
handle_neuropsychological_symptoms(parsed, document, lits)

add_header(document, "Συμπεράσματα", 2)
handle_conclusions(parsed, document, lits)

handle_signature(document)

# Save the document
document.save('output.docx')
