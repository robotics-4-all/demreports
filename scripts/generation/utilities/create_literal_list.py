# pylint: disable=C0301

def create_literal_list(items, add_identifiers=False):
    """
    Creates a string representation of a list of items, formatted with commas and the word "και" before the last item.

    Args:
        items (list): A list of strings to be joined.

    Returns:
        str: A string representation of the list. If the list is empty, returns an empty string. If the list contains one item, returns that item. Otherwise, returns the items joined by commas, with "και" before the last item.
    """
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    
    identifiers = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ"]
    final = ""
    for i, item in enumerate(items):
        if i == len(items) - 1:
            break
        if add_identifiers:
            final += identifiers[i] + ") " + item + ", "
        else:
            final += item + ", "
    
    if add_identifiers:
        final+= "καθώς και " + identifiers[len(items) - 1] + ") " + items[-1]
    else:
        final+= "καθώς και " + items[-1]
    # return ", ".join(items[:-1]) + ", καθώς και " + items[-1]
    return final
