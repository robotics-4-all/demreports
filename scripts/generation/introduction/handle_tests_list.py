# pylint: disable=C0301

def handle_tests_list(parsed, document):
    """
    Adds a list of test descriptions to a document based on the keys present in the parsed dictionary.

    Args:
        parsed (dict): A dictionary containing keys that represent different tests.
        document (Document): A Document object where the test descriptions will be added.

    The function checks for the presence of specific keys in the parsed dictionary and adds corresponding
    test descriptions to the document as bullet points. The descriptions are in Greek, except for the BDI test.
    
    The keys and their corresponding descriptions are:
        - 'mmse': 'Σύντομη εξέταση της νοητικής κατάστασης MMSE'
        - 'ravlt': 'Δοκιμασία λεκτικής ακουστικής μάθησης RAVLT'
        - 'rocft': 'Δοκιμασία σύνθετης φιγούρας ROCFT'
        - 'fucas': 'Δοκιμασία νοητικής λειτουργικής εκτίμησης FUCAS'
        - 'frssd': 'Κλίμακα λειτουργικής εκτίμησης συμπτωμάτων άνοιας FRSSD'
        - 'npi': 'Κλίμακα Νευροψυχιατρικών Συμπτωμάτων NPI'
        - 'gds': 'Γηριατρική κλίμακα κατάθλιψης GDS'
        - 'sast': 'Ερωτηματολόγιο εκτίμησης άγχους SAST'
        - 'bdi': 'Beck Depression Inventory BDI'
    """

    p2 = document.add_paragraph()
    if 'mmse' in parsed and parsed['mmse'].administered:
        mmse_lit = 'MMSE' if parsed['patient'].education > 4 else 'HMSE'
        p2.add_run(f'•  Σύντομη εξέταση της νοητικής κατάστασης {mmse_lit}\n').bold = True
    if 'ravlt' in parsed and parsed['ravlt'].administered:
        p2.add_run('•  Δοκιμασία λεκτικής ακουστικής μάθησης RAVLT\n').bold = True
    if 'rocft' in parsed and parsed['rocft'].administered:
        p2.add_run('•  Δοκιμασία σύνθετης φιγούρας ROCFT\n').bold = True
    if 'fucas' in parsed and parsed['fucas'].administered:
        p2.add_run('•  Δοκιμασία νοητικής λειτουργικής εκτίμησης FUCAS\n').bold = True
    if 'frssd' in parsed and parsed['frssd'].administered:
        p2.add_run('•  Κλίμακα λειτουργικής εκτίμησης συμπτωμάτων άνοιας FRSSD\n').bold = True
    if 'npi' in parsed and parsed['npi'].administered:
        p2.add_run('•  Κλίμακα Νευροψυχιατρικών Συμπτωμάτων NPI\n').bold = True
    if 'gds' in parsed and parsed['gds'].administered:
        p2.add_run('•  Γηριατρική κλίμακα κατάθλιψης GDS\n').bold = True
    if 'sast' in parsed and parsed['sast'].administered:
        p2.add_run('•  Ερωτηματολόγιο εκτίμησης άγχους SAST\n').bold = True
    if 'bdi' in parsed and parsed['bdi'].administered:
        p2.add_run('•  Beck Depression Inventory BDI\n').bold = True
