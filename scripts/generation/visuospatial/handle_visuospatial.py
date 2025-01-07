# pylint: disable=C0301

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor

from generation.tests_literals.rocft_literals import rocft_literals

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
    # check we have ROCFT data
    if 'rocft' not in parsed or parsed['rocft'].administered == False:
        return

    rocft_lits = rocft_literals(parsed['rocft'], parsed['patient'].age, parsed['patient'].education)
    mmse_lit = ""
    if parsed['mmse'].administered:
        if parsed['mmse'].v_score == 0 and rocft_lits['copy_flag']:
            mmse_lit = f"Σε αντίστοιχο οπτικοχωρικό υπο-έργο της MMSE, {literals['full_with_article']} παρουσίασε επίσης ελλείψεις. "
        if parsed['mmse'].v_score == 1 and not rocft_lits['copy_flag']:
            mmse_lit = f"Σε αντίστοιχο οπτικοχωρικό υπο-έργο της MMSE, {literals['full_with_article']} σημείωσε επίσης φυσιολογική επίδοση. "

    problems = ""
    if not rocft_lits['copy_flag']:
        problems = "δεν παρουσίασε αντιληπτικές/οπτικοχωρικές δυσκολίες στον χώρο"
    else:
        problems = "παρουσίασε αντιληπτικές/οπτικοχωρικές δυσκολίες, οι οποίες ήταν πιθανόν να επιφέρουν προβλήματα κατά τη διάρκεια της βάδισης, όπως για παράδειγμα πτώσεις πάνω σε αντικείμενα, δυσκολίες αναγνώρισης αντικειμένων ή αναγνώριση της θέσεως των αντικειμένων, καθώς επίσης και δυσκολίες στην εύρεση αντικειμένων μέσα στο χώρο"

    p1 = document.add_paragraph()

    # input from Elena
    p1.add_run(f"{literals['full_with_article_capital']}, {rocft_lits['copy_problem']} δυσκολίες στην αναπαραγωγή σύνθετων οπτικοχωρικών έργων, όπως διαπιστώθηκε μέσω της δοκιμασίας οπτικοχωρικής αντίληψης και μνήμης ROCFT. {mmse_lit}Τα παραπάνω ευρήματα συνηγορούν ότι για το χρονικό διάστημα στο οποίο αναφέρεται η εκτίμηση {literals['full_with_article']} {problems}. ")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
