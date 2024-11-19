"""
File handling the generation of the neuropsychological symptoms report paragraph
"""
# pylint: disable=C0301
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

from generation.tests_literals.gds_literals import gds_literals
from generation.tests_literals.npi_literals import npi_literals
from generation.utilities.create_literal_list import create_literal_list

def handle_neuropsychological_symptoms(parsed, document, literals):
    """
    Handles the generation of a neuropsychological symptoms report paragraph in a document.
    Args:
        parsed (dict): A dictionary containing parsed data, including 'gds' key for GDS literals.
        document (Document): A python-docx Document object where the paragraph will be added.
        literals (dict): A dictionary containing various literals used in the report, such as 'examinee_gender_v2', 'att_literal_1', and 'att_names_with_relations'.
        print_output (bool, optional): If True, prints the output. Defaults to False.
    Returns:
        None
    """
    p1 = document.add_paragraph()

    gds_lits = gds_literals(parsed['gds'])

    p1.add_run(f"Σύμφωνα με τα ερωτηματολόγιο αυτοαναφοράς (GDS) που χορηγήθηκε {literals['examinee_gender_v2']}, για την περίοδο που έγινε η εκτίμηση, {gds_lits}.")

    npi_lits = npi_literals(parsed['npi'])

    atts_related = f"{literals['att_literal_1']} ({literals['att_names_with_relations']})" if literals['att_names_with_relations'] != "" else literals['the_same_v3']

    p1.add_run(f" Σύμφωνα με {atts_related}")
    if len(npi_lits[3]) > 0:
        p1.add_run(" αναφέρθηκαν συμπεριφορές")
        p1.add_run(" μεγάλης σοβαρότητας").bold = True
        p1.add_run(" όπως ")
        p1.add_run(create_literal_list(npi_lits[3]))
        p1.add_run(". ")
    if len(npi_lits[2]) > 0:
        is_first = len(npi_lits[3]) == 0
        is_last = len(npi_lits[1]) == 0
        ll = ""
        if is_last:
            ll = 'Τέλος'
        if not is_last and not is_first:
            ll = 'Επίσης'

        p1.add_run(f"{ll} αναφέρθηκαν συμπεριφορές")
        p1.add_run(" μέτριας σοβαρότητας").bold = True
        p1.add_run(" όπως ")
        p1.add_run(create_literal_list(npi_lits[2]))
        p1.add_run(". ")
    if len(npi_lits[1]) > 0:
        is_only = len(npi_lits[3]) == 0 or len(npi_lits[2]) == 0
        ll = ""
        if not is_only:
            ll = 'Τέλος'
        p1.add_run(f"{ll} αναφέρθηκαν συμπεριφορές")
        p1.add_run(" ήπιας σοβαρότητας").bold = True
        p1.add_run(" όπως ")
        p1.add_run(create_literal_list(npi_lits[1]))
        p1.add_run(". ")

    if len(npi_lits[1]) == 0 and len(npi_lits[2]) == 0 and len(npi_lits[3]) == 0:
        p1.add_run(" δεν αναφέρθηκαν ").bold = True
        p1.add_run(f"νευροψυχιατρικά συμπτώματα σχετικά με {npi_lits['all']}. ")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
