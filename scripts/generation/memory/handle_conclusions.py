"""
File that handles the generation of the memory conclusions paragraph
"""
# pylint: disable=C0301

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor

from generation.tests_literals.ravlt_literals import ravlt_literals
from generation.tests_literals.rocft_literals import rocft_literals

def handle_memory_conclusions(parsed, document, literals):
    """
    Generates a paragraph summarizing memory performance conclusions and adds it to the given document.

    Args:
        parsed (dict): A dictionary containing parsed data, including 'ravlt', 'rocft', and 'patient' information.
        document (Document): A python-docx Document object where the paragraph will be added.
        literals (dict): A dictionary containing literal strings for gender and articles to be used in the text.
        print_output (bool, optional): If True, prints the generated paragraph text. Defaults to False.

    Returns:
        None
    """
    p1 = document.add_paragraph()

    ravlt_lits = ravlt_literals(parsed['ravlt'], parsed['patient'].age)
    rocft_lits = rocft_literals(parsed['rocft'], parsed['patient'].age, parsed['patient'].education)

    rocft_recall_problem = ", αλλά και συγκράτησης καινούριων πληροφοριών προκειμένου να ανασύρει από την μακρόχρονη μνήμη αποτελεσματικά νέες πληροφορίες" if (rocft_lits["recall_problem"] or ravlt_lits["maintain_problem"]) else ""
    rocft_problem = f" Τα ελλείμματα σε επίπεδο οπτικής μνήμης επεισοδίων, μεταφράζονται σε δυσκολίες {literals['examinee_gender']} να θυμηθεί τον χώρο που έχει τοποθετήσει προσωπικά {literals['article_v3']} αντικείμενα, το σημείο στο οποίο βρίσκεται ένα συγκεκριμένο σούπερ μάρκετ κτλ." if rocft_lits["copy_problem"] or rocft_lits["recall_problem"] else ""
    ravlt_problem = f" Σε επίπεδο καθημερινής ζωής τα παραπάνω ελλείμματα μεταφράζονται σε δυσκολία {literals['examinee_gender']} να θυμηθεί πληροφορίες που έχουν επεξεργαστεί λεκτικά, όπως να θυμηθεί συζητήσεις τις οποίες έχει κάνει, πληροφορίες τις οποίες άκουσε στην τηλεόραση, ποιος είναι ο κωδικός από το κινητό τηλέφωνο, ποιος είναι ο καινούριος τηλεφωνικός αριθμός της κόρης κτλ." if ravlt_lits["learning_problem"] or ravlt_lits["maintain_problem"] else ""

    problem_in_general = " μη ύπαρξης" if not (rocft_lits["recall_problem"] or rocft_lits["copy_problem"] or ravlt_lits["learning_problem"] or ravlt_lits["maintain_problem"]) else " ύπαρξης"

    verbal_bool = ravlt_lits["learning_problem"] or ravlt_lits["maintain_problem"]
    visual_bool = rocft_lits["recall_problem"] or rocft_lits["copy_problem"]

    problems_verbal = "λεκτικής"
    problems_visual = "οπτικής"

    problems = ""
    if verbal_bool and visual_bool and parsed['ravlt'].administered and parsed['rocft'].administered:
        problems = f"{problems_verbal} και {problems_visual}"
    elif verbal_bool and not visual_bool and parsed['ravlt'].administered:
        problems = problems_verbal
    elif visual_bool and not verbal_bool and parsed['rocft'].administered:
        problems = problems_visual
    else:
        problems = f"{problems_verbal} και {problems_visual}"

    text = f"Οι παραπάνω επιδόσεις στην μνήμη επεισοδίων συνηγορούν υπέρ{problem_in_general} δυσκολιών από την πλευρά {literals['examinee_gender']} όσον αφορά στην ικανότητα {problems} μάθησης{rocft_recall_problem}.{ravlt_problem}{rocft_problem}"
    p1.add_run(text)

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
