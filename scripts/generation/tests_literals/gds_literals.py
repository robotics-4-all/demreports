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
        return "δεν διαπιστώθηκε διαταραχή της διάθεσης"
    elif results.score <= 8:
        return "διαπιστώθηκε διαταραχή της διάθεσης σε επίπεδο ήπιας κατάθλιψης"
    elif results.score <= 11:
        return "διαταραχή της διάθεσης σε επίπεδο μέτριας κατάθλιψης"

    return "διαταραχή της διάθεσης σε επίπεδο σοβαρής κατάθλιψης"
