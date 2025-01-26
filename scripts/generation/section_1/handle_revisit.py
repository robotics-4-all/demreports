"""
File that contains the function to handle the revisit paragraph of section 1.
"""

# pylint: disable=C0301
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def handle_s1_revisit(parsed, document, literals):
    """
    Handles the generation of a paragraph in the document for a patient's revisit.

    This function checks if the patient has a revisit entry. If so, it adds a paragraph
    to the document detailing the revisit information, including the date of revisit,
    the effectiveness of the cognitive intervention, daily functionality, and behavior
    disturbances based on information from an attendant.

    Args:
        parsed (dict): A dictionary containing parsed data, including patient information.
        document (Document): The document object where the paragraph will be added.
        literals (dict): A dictionary containing literal values to be inserted into the paragraph.

    Returns:
        None
    """
    if not parsed['patient'].revisit:
        return

    p1 = document.add_paragraph()

    atts_related = f"καθώς και μέσα από πληροφορίες που ελήφθησαν από {literals['att_literal_1']}"

    p1.add_run(f"Η ίδια εκτίμηση διενεργήθηκε στα πλαίσια ελέγχου ρουτίνας μετά από {literals['revisit_after']} στις {literals['revisit_date']}, με την χρήση της ίδιας συστοιχίας. Η καθημερινή λειτουργικότητα ελέγχθηκε με αντικειμενικό τρόπο (εκτίμηση {literals['the_same_v2']}) {atts_related}. Όσον αφορά τις διαταραχές συμπεριφοράς, οι πληροφορίες ελήφθησαν επίσης από {literals['att_literal_1']} {literals['att_names']}.")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
