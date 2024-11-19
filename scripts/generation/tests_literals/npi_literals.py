"""
File containing the literals for the NPI test cases
"""
# pylint: disable=C0301
from generation.utilities.create_literal_list import create_literal_list

def npi_literals(results):
    """
    Generates a dictionary categorizing neuropsychiatric symptoms based on their severity and frequency.
    Args:
        results (object): An object containing attributes for each behavior's frequency and severity.
                          Expected attributes are:
                          - delusions_freq, delusions_severity
                          - hallucinations_freq, hallucinations_severity
                          - agitation_freq, agitation_severity
                          - depression_freq, depression_severity
                          - elation_freq, elation_severity
                          - apathy_freq, apathy_severity
                          - disinhibition_freq, disinhibition_severity
                          - irritability_freq, irritability_severity
                          - aberrant_motor_activity_freq, aberrant_motor_activity_severity
                          - sleep_freq, sleep_severity
                          - appetite_freq, appetite_severity
    Returns:
        dict: A dictionary with severity levels as keys (0, 1, 2, 3, 'all') and lists of strings describing
              the behaviors and their frequencies as values. The 'all' key contains a list of all behaviors.
    """
    freqs = {
        0: "",
        1: "λιγότερο από μια φορά την εβδομάδα",
        2: "περίπου μια φορά την εβδομάδα",
        3: "αρκετές φορές την εβδομάδα αλλά λιγότερο από μια φορά τη μέρα",
        4: "μία φορά ή περισσότερες τη μέρα",
    }

    behaviors = {
        'delusions': "παραισθήσεις",
        'hallucinations': "ψευδαισθήσεις",
        'agitation': "επιθετικότητα",
        'depression': "κατάθλιψη",
        'elation': "ευφορία",
        'apathy': "απάθεια/αδιαφορία",
        'disinhibition': "έλλειψη αναστολών",
        'irritability': "ευερεθιστότητα",
        'aberrant_motor_activity': "παθολογική κινητική συμπεριφορά",
        'sleep': "διαταραχές συμπεριφοράς την νύχτα",
        'appetite': "διαταραχές διατροφής",
    }

    severity_items = {
        0: [],
        1: [],
        2: [],
        3: [],
        'all': create_literal_list([value for value in behaviors.values()])
    }

    for key, value in behaviors.items():
        if getattr(results, f"{key}_freq") > 0: # we have a problem here
            literal_freq = freqs[getattr(results, f'{key}_freq')]
            severity_items[getattr(results, f"{key}_severity")].append(
                f"{value} με συχνότητα εμφάνισης {literal_freq}"
            )
    
    return severity_items

