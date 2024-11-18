def add_header(document, string, level=1):
    """
    Adds a header to the given document with the specified string.

    Args:
        document: The document object to which the header will be added.
        string (str): The text to be added as a header.

    The header text will be bold and underlined, and the paragraph will be center-aligned.
    """
    p0 = document.add_paragraph()
    r1_p1 = p0.add_run(f'{string}')
    r1_p1.bold = True if level == 1 else False
    r1_p1.underline = True
    p0.alignment = 1//level # center align the paragraph
