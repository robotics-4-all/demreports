"""
File that contains the function to handle the generation of the conclusions section in a document.
"""

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor
# pylint: disable=C0301

def handle_conclusions(parsed, document, literals):
    """
    Handles the generation of the conclusions section in a document.

    Args:
        parsed (dict): Parsed data to be used in the conclusions.
        document (Document): The document object where the conclusions will be added.
        literals (dict): A dictionary containing literal values to be inserted into the text.
        print_output (bool, optional): If True, prints the output. Defaults to False.

    Returns:
        None
    """
    p1 = document.add_paragraph()

    # input from Elena
    p1.add_run(f"Η συνολική εκτίμηση για την χρονική περίοδο στην οποία αναφέρεται η εξέταση, συνηγορεί υπέρ νοητικών ελλειμμάτων στην λεκτική και οπτική επεισοδιακή μνήμη, στις οπτικοχωρικές ικανότητες, καθώς και δυσκολίες σε πλευρές της εκτελεστικής λειτουργίας. Τα ελλείμματα αυτά μέσα από την άμεση εκτίμηση {literals['the_same']} φαίνεται ότι επηρέαζαν σημαντικά την ικανότητα {literals['examinee_gender']} για καθημερινή αυτοεξυπηρέτηση όσον αφορά τις σύνθετες δραστηριότητες της καθημερινής ζωής που απαιτούσαν σύνθετη σκέψη, ενώ οι πιο απλές δραστηριότητες διατηρούνταν σε καλύτερο βαθμό (τουλάχιστον όσες ελέγχθηκαν, δηλαδή η ικανότητα ένδυσης και πλύσης των χεριών). Σύμφωνα με {literals['att_literal_1']} {literals['article_lastname_mr_mrs']} για την περίοδο που έλαβε χώρα η εκτίμηση, είχε έκπτωση και σε πιο απλές δραστηριότητες της καθημερινής ζωής, ενώ παρουσίασε και σημαντικές διαταραχές συμπεριφοράς. Βάσει του συνόλου της εξέτασης καθώς επίσης και των πληροφοριών που αντλήθηκαν από {literals['att_literal_1']}, {literals['article_lastname_mr_mrs']} για το διάστημα το οποίο διενεργήθηκε η νευροψυχολογική εκτίμηση, χρειαζόταν υπενθύμιση και βοήθεια προκειμένου να ανταπεξέρχεται και να εκτελεί σωστά τα σύνθετα έργα της καθημερινής ζωής.") 

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
    p1.runs[0].font.color.rgb = RGBColor(255, 0, 0)
