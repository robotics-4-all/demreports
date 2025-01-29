"""
File that contains the function to handle the last paragraph of section 1.
"""

# pylint: disable=C0301
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def handle_s1_last(parsed, document, literals):
    """
    Handles the generation of the last section of the document for section 1.

    Args:
        parsed (dict): A dictionary containing parsed data, including patient information.
        document (Document): A python-docx Document object where the paragraph will be added.
        literals (dict): A dictionary containing literal values such as 'article_v2', 'last_name', and 'examinee_gender'.
        print_output (bool, optional): If True, prints the output. Defaults to False.

    Returns:
        None
    """
    p1 = document.add_paragraph()

    revisit = "" if not parsed['patient'].revisit else ", εκ νέου"

    p1.add_run(f"\nΜετά την ολοκλήρωση της νευροψυχολογικής εκτίμησης και κατά τη διάρκεια της ανακοίνωσης των αποτελεσμάτων {literals['article_v2']} κ. {literals['last_name']}, συστάθηκε{revisit} συμμετοχή {literals['examinee_gender']} σε προγράμματα νοητικής ενδυνάμωσης, καθώς και επανέλεγχος σε ένα έτος.")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
