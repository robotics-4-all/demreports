from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from generation.tests_literals.ravlt_literals import ravlt_literals

def handle_verbal_memory(parsed, document, literals, print_output = False):
    # check we have RAVLT data
    if 'ravlt' not in parsed:
        return

    ravlt_lits = ravlt_literals(parsed['ravlt'], parsed['patient'].age)
    p1 = document.add_paragraph()

    p1_r1 = p1.add_run("Επεισοδιακή λεκτική μνήμη: ")
    p1_r1.italic = True

    printable = f"Κατά τη νευροψυχολογική εκτίμηση στις {parsed['patient'].date_npse} και συγκεκριμένα μέσω της χορήγησης της δοκιμασίας RAVLT, {literals['full_with_article']} {ravlt_lits['learning']} στην ικανότητα μάθησης καταλόγου λέξεων μετά από επανάληψη. Το παραπάνω γεγονός καταδείκνυε ότι για το διάστημα στο οποίο έγινε η εκτίμηση, {ravlt_lits['learning_explanation']}. Η ικανότητα ανάσυρσης της πληροφορίας από την μακρόχρονη μνήμη, όπως διαπιστώθηκε από την ίδια δοκιμασία, {ravlt_lits['maintain']}, καθώς {literals['full_with_article']} {ravlt_lits['maintain_explanation']}. "

    p1.add_run(printable)

    if print_output:
        print(printable)

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY