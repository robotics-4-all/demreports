from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
# pylint: disable=C0301

def handle_signature(document):
    """
    Adds a signature section to the given document.

    This function creates a new paragraph in the document and adds multiple
    lines of text to it, including a signature line and various titles and
    qualifications. The paragraph is then center-aligned.

    Args:
        document (Document): The document object to which the signature
                             section will be added.
    """
    p1 = document.add_paragraph()

    # input from Elena
    p1.add_run("\n\nΥπογραφή\n\n\n\n\n")
    p1.add_run("Πόπτση Ελένη\n")
    p1.add_run("PhD Γνωστικής Ψυχολογίας ΑΠΘ\n")
    p1.add_run("Ψυχολόγος ΑΠΘ\n")
    p1.add_run("MSc Κοινωνικής Ψυχιατρικής ΔΠΘ\n")

    p1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
