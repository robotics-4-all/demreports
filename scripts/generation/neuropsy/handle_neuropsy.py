from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor

from generation.tests_literals.gds_literals import gds_literals

def handle_neuropsychological_symptoms(parsed, document, literals, print_output = False):
    p1 = document.add_paragraph()

    gds_lits = gds_literals(parsed['gds'])

    # input from Elena
    p1.add_run(f"Σύμφωνα με τα ερωτηματολόγιο αυτοαναφοράς (GDS) που χορηγήθηκε {literals['examinee_gender_v2']}, για την περίοδο που έγινε η εκτίμηση, {gds_lits}.")
    
    p1.add_run(f" Σύμφωνα με {literals['att_literal_1']} ({literals['att_names_with_relations']}) αναφέρθηκαν ήπιας σοβαρότητας κατάθλιψη με συχνότητα εμφάνισης μία φορά ή περισσότερες την ημέρα, καθώς και ήπιας σοβαρότητας απάθεια με συχνότητα εμφάνισης αρκετές φορές την εβδομάδα αλλά λιγότερο από µια φορά την ημέρα. Αναφέρθηκαν επίσης μέτριας σοβαρότητας επιθετικότητα, άγχος, έλλειψη αναστολών, ευερεθιστότητα καθώς και παθολογική κινητική συμπεριφορά. Οι παραπάνω συμπεριφορές αναφέρθηκε από τους συνοδούς ότι παρατηρήθηκαν πολύ συχνά, μία ή περισσότερες φορές την ημέρα. Τέλος αναφέρθηκε ήπια απάθεια/αδιαφορία με συχνότητα εμφάνισης αρκετές φορές την εβδομάδα αλλά λιγότερο από µια φορά την ημέρα. ") 

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
    p1.runs[-1].font.color.rgb = RGBColor(255, 0, 0)