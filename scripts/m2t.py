"""
Implements the logic for the model to text transformation.
"""
# pylint: disable=C0301

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
import os

# Create a new document
current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.docx')
document = Document(input_path)

# Load the metamodel and model
my_metamodel = metamodel_from_file('../syntax/demreport.tx')
my_model = my_metamodel.model_from_file('../examples/test.drep')
parsed = parse_model(my_model)

lits = generate_literals(parsed)

# Call the functions to handle the parsed data
handle_exam(parsed, document)

add_header(document, "Στοιχεία ασθενή\n") # ok
handle_patient_info(parsed, document) # ok

add_header(document, "Δοκιμασίες\n") # ok
handle_tests_list(parsed, document) # ok

add_header(document, "Αποτελέσματα\n") # ok
handle_scores(parsed, document) # ok

add_header(document, "\nΕισαγωγή\n") # ok
handle_s1_first_visit(parsed, document, lits) #οk
handle_s1_revisit(parsed, document, lits) #ok
handle_s1_last(parsed, document, lits) #ok

add_header(document, "\nΑποτελέσματα νευροψυχολογικής εκτίμησης")
if parsed['ravlt'].administered or parsed['rocft'].administered:
    add_header(document, "\nΜνήμη επεισοδίων", 2)
    if parsed['ravlt'].administered:
        handle_verbal_memory(parsed, document, lits) #ok
    if parsed['rocft'].administered:
        handle_visual_memory(parsed, document, lits) #ok
    handle_memory_conclusions(parsed, document, lits)

if parsed['rocft'].administered:
    add_header(document, "\nΟπτικοχωρικές ικανότητες\n", 2)
    handle_visuospatial(parsed, document, lits)

if parsed['fucas'].administered:
    add_header(document, "\nΕκτελεστικές λειτουργίες\n", 2)
    handle_executive_functions(parsed, document, lits)

if parsed['frssd'].administered or parsed['fucas'].administered:
    add_header(document, "\nΚαθημερινή λειτουργικότητα\n", 2)
    handle_everyday_functionality(parsed, document, lits)

if parsed['gds'].administered or parsed['npi'].administered:
    add_header(document, "\nΝευροψυχιατρικά συμπτώματα\n", 2)
    handle_neuropsychological_symptoms(parsed, document, lits)

add_header(document, "\nΣυμπεράσματα\n", 2)
handle_conclusions(parsed, document, lits)

handle_signature(document)

# Save the document
document.save('output.docx')
