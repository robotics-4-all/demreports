"""
File handling the generation of the neuropsychological symptoms report paragraph
"""

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor

from generation.tests_literals.gds_literals import gds_literals

def handle_neuropsychological_symptoms(parsed, document, literals, print_output = False):
    def handle_neuropsychological_symptoms(parsed, document, literals, print_output=False):
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
    
    p1.add_run(f" Σύμφωνα με {literals['att_literal_1']} ({literals['att_names_with_relations']}) αναφέρθηκαν ήπιας σοβαρότητας κατάθλιψη με συχνότητα εμφάνισης μία φορά ή περισσότερες την ημέρα, καθώς και ήπιας σοβαρότητας απάθεια με συχνότητα εμφάνισης αρκετές φορές την εβδομάδα αλλά λιγότερο από µια φορά την ημέρα. Αναφέρθηκαν επίσης μέτριας σοβαρότητας επιθετικότητα, άγχος, έλλειψη αναστολών, ευερεθιστότητα καθώς και παθολογική κινητική συμπεριφορά. Οι παραπάνω συμπεριφορές αναφέρθηκε από τους συνοδούς ότι παρατηρήθηκαν πολύ συχνά, μία ή περισσότερες φορές την ημέρα. Τέλος αναφέρθηκε ήπια απάθεια/αδιαφορία με συχνότητα εμφάνισης αρκετές φορές την εβδομάδα αλλά λιγότερο από µια φορά την ημέρα. ")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
    p1.runs[-1].font.color.rgb = RGBColor(255, 0, 0)
