from datetime import datetime

# Function to compare two dates
def compare_dates(date1_str, date2_str):
    """
    Compares two dates given as strings in the format "dd/mm/yyyy".

    Args:
        date1_str (str): The first date string.
        date2_str (str): The second date string.

    Returns:
        int: Returns 0 if the first date is earlier than the second date,
             returns 2 if the first date is later than the second date,
             returns 1 if both dates are the same.
    """
    # Parse the strings into datetime objects
    date1 = datetime.strptime(date1_str, "%d/%m/%Y")
    date2 = datetime.strptime(date2_str, "%d/%m/%Y")

    # Compare the dates
    if date1 < date2:
        return 0
    elif date1 > date2:
        return 2
    else:
        return 1
