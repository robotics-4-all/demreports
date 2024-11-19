# pylint: disable=C0301

def handle_patient_info(parsed, document):
    """
    Processes patient information and adds it to the given document.

    Args:
        parsed (dict): A dictionary containing parsed patient data. 
                       Expected to have a 'patient' key with an object that has 
                       'name', 'surname', 'amka', 'age', 'education', and 'enesthesia' attributes.
        document (Document): A document object where the patient information will be added.

    Returns:
        None
    """
    patient = parsed['patient']

    p1 = document.add_paragraph()
    r1_p2 = p1.add_run('ΟΝΟΜΑΤΕΠΩΝΥΜΟ:\t')
    r1_p2.bold = True
    p1.add_run(f"{patient.name} {patient.surname}\n")

    r1_p3 = p1.add_run('ΑΜΚΑ:\t\t\t')
    r1_p3.bold = True
    p1.add_run(f"{patient.amka}\n" if patient.amka != "" else "-\n")

    r1_p4 = p1.add_run('ΗΛΙΚΙΑ:\t\t')
    r1_p4.bold = True
    p1.add_run(f"{patient.age} ΕΤΩΝ\n")

    r1_p5 = p1.add_run('ΕΚΠΑΙΔΕΥΣΗ:\t\t')
    r1_p5.bold = True
    p1.add_run(f"{patient.education} ΕΤΗ\n")

    r1_p6 = p1.add_run('ΕΝΑΙΣΘΗΣΙΑ:\t\t')
    r1_p6.bold = True
    p1.add_run('ΝΑΙ' if patient.enesthesia else 'ΟΧΙ\n')

    p1.alignment = 0 # left align the paragraph
