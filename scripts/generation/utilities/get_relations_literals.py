"""
File that contains the function to get relationship literals in Greek.
"""

# pylint: disable=C0301

def get_relations_literals():
    """
    Returns a dictionary containing relationship literals in Greek.

    The dictionary has two keys: "child" and "sibling". Each key maps to another dictionary
    that contains the Greek terms for the relationship based on gender:
    - "F" for female
    - "M" for male

    Returns:
        dict: A dictionary with relationship literals in Greek.
    """
    ret = {}
    ret["child"] = {
        "F": "κόρη",
        "M": "γιος"
    }
    ret["sibling"] = {
        "F": "αδελφή",
        "M": "αδελφός"
    }
    ret["parent"] = {
        "F": "μητέρα",
        "M": "πατέρας"
    }
    ret["husband"] = {
        "F": "σύζυγος",
        "M": "σύζυγος"
    }
    return ret

# transform 2024-11-18 to 18/11/2024
def transform_date(date):
    """
    Transforms a date from the format "YYYY-MM-DD" to "DD/MM/YYYY".

    Args:
        date (str): A string representing a date in the format "YYYY-MM-DD".

    Returns:
        str: A string representing the date in the format "DD/MM/YYYY".
    """
    return date[-2:] + "/" + date[5:7] + "/" + date[:4]
