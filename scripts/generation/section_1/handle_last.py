# pylint: disable=C0301
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def handle_s1_last(parsed, document, literals, print_output = False):
    p1 = document.add_paragraph()

    revisit = "" if not parsed['patient'].revisit else ", εκ νέου"

    p1.add_run(f"Μετά την ολοκλήρωση της νευροψυχολογικής εκτίμησης και κατά τη διάρκεια της ανακοίνωσης των αποτελεσμάτων {literals['article_v2']} κ. {literals['last_name']}, συστάθηκε{revisit} συμμετοχή {literals['examinee_gender']} σε προγράμματα νοητικής ενδυνάμωσης, καθώς και επανέλεγχος σε ένα έτος.")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
