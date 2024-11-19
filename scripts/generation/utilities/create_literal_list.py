def create_literal_list(items):
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
    return ", ".join(items[:-1]) + " και " + items[-1]
