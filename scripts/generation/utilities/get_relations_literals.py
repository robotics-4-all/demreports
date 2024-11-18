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
