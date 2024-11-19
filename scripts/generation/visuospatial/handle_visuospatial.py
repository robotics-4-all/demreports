# pylint: disable=C0301

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor

def handle_visuospatial(parsed, document, literals):
    """
    Handles the visuospatial section of the report by adding a paragraph to the document.
    Args:
        parsed (dict): Parsed data from the input source.
        document (Document): The document object where the paragraph will be added.
        literals (dict): A dictionary containing literal strings used in the paragraph.
        print_output (bool, optional): If True, prints the output. Defaults to False.
    Returns:
        None
    """
    p1 = document.add_paragraph()

    # input from Elena
    p1.add_run(f"{literals['full_with_article_capital']}, δεν παρουσίασε δυσκολίες στην αναπαραγωγή σύνθετων οπτικοχωρικών έργων, όπως διαπιστώθηκε μέσω της δοκιμασίας οπτικοχωρικής αντίληψης και μνήμης ROCFT. Σε αντίστοιχο οπτικοχωρικό υπο-έργο της MMSE, {literals['full_with_article']} σημείωσε επίσης φυσιολογική επίδοση. Τα παραπάνω ευρήματα συνηγορούν ότι για το χρονικό διάστημα στο οποίο αναφέρεται η εκτίμηση {literals['full_with_article']} δεν παρουσίασε αντιληπτικές/οπτικοχωρικές δυσκολίες στον χώρο. ")

    p1.runs[0].font.color.rgb = RGBColor(255, 0, 0)
    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
