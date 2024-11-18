from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def handle_visuospatial(parsed, document, literals, print_output = False):
    p1 = document.add_paragraph()

    # input from Elena
    p1.add_run(f"{literals['full_with_article_capital']}, δεν παρουσίασε δυσκολίες στην αναπαραγωγή σύνθετων οπτικοχωρικών έργων, όπως διαπιστώθηκε μέσω της δοκιμασίας οπτικοχωρικής αντίληψης και μνήμης ROCFT. Σε αντίστοιχο οπτικοχωρικό υπο-έργο της MMSE, {literals['full_with_article']} σημείωσε επίσης φυσιολογική επίδοση. Τα παραπάνω ευρήματα συνηγορούν ότι για το χρονικό διάστημα στο οποίο αναφέρεται η εκτίμηση {literals['full_with_article']} δεν παρουσίασε αντιληπτικές/οπτικοχωρικές δυσκολίες στον χώρο. ")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY