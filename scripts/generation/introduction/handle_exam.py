def handle_exam(parsed, document):
    """
    Handles the addition of report information to a document.

    This function adds two paragraphs to the provided document:
    1. The first paragraph contains the location 'Θεσσαλονίκη' in bold and the report date, right-aligned.
    2. The second paragraph contains the text 'Στοιχεία ασθενή' in bold, center-aligned.

    Args:
        parsed (dict): A dictionary containing parsed report data. Expected to have a 'report' key with a 'date' field.
        document (Document): A python-docx Document object where the paragraphs will be added.

    Returns:
        None
    """
    p1 = document.add_paragraph()
    r1_p1 = p1.add_run('Θεσσαλονίκη ')
    r1_p1.bold = True
    p1.add_run(f"{parsed['report'].date}\n")
    p1.alignment = 2 # right align the paragraph
    