"""
File containing the literals for the GDS test cases
"""
# pylint: disable=C0301

def gds_literals(results):
    """
    Generates a descriptive string based on the Geriatric Depression Scale (GDS) score.

    Parameters:
    results (object): An object that contains a 'score' attribute representing the GDS score.

    Returns:
    str: A string describing the level of mood disorder based on the GDS score.
         - If score <= 5: "δεν διαπιστώθηκε διαταραχή της διάθεσης (score/15)"
         - If score <= 8: "διαπιστώθηκε διαταραχή της διάθεσης σε επίπεδο υποκατάθλιψης (score/15)"
         - If score <= 11: "διαταραχή της διάθεσης σε επίπεδο μέτριας κατάθλιψης (score/15)"
         - If score > 11: "διαταραχή της διάθεσης σε επίπεδο σοβαρής κατάθλιψης (score/15)"
    """
    if results.score <= 5:
        return f"δεν διαπιστώθηκε διαταραχή της διάθεσης ({results.score}/15)"
    elif results.score <= 8:
        return f"διαπιστώθηκε διαταραχή της διάθεσης σε επίπεδο υποκατάθλιψης ({results.score}/15)"
    elif results.score <= 11:
        return f"διαταραχή της διάθεσης σε επίπεδο μέτριας κατάθλιψης ({results.score}/15)"

    return f"διαταραχή της διάθεσης σε επίπεδο σοβαρής κατάθλιψης ({results.score}/15)"
