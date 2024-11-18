from datetime import datetime

def date_difference(date1, date2):
    """
    Calculate the difference between two dates and return it as a human-readable string.
    Args:
        date1 (str): The first date in the format "dd/mm/yyyy".
        date2 (str): The second date in the format "dd/mm/yyyy".
    Returns:
        str: A string representing the difference between the two dates in years, months, or days.
             The string is in Greek and uses the terms "έτη" (years), "μήνες" (months), and "ημέρες" (days).
             If the difference is more than 6 months, it rounds up to the next year.
    """
    # Parse the dates from string format to datetime objects
    date_format = "%d/%m/%Y"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    # Ensure d1 is the earlier date
    if d1 > d2:
        d1, d2 = d2, d1

    # Calculate differences in years, months, and days
    years = d2.year - d1.year
    months = d2.month - d1.month
    days = d2.day - d1.day

    # Adjust if days are negative
    if days < 0:
        months -= 1
        # Add the number of days in the previous month (from d1's month to d2's month)
        days += (d1.replace(month=(d1.month % 12) + 1, day=1) - d1).days

    # Adjust if months are negative
    if months < 0:
        years -= 1
        months += 12

    # Construct the final difference string
    difference = ""
    if years > 0:
        if months > 6:
            years += 1
        difference = f"περίπου {years} έτη"
    elif months > 0:
        difference = f"περίπου {months} μήνες"
    elif days > 0:
        difference = f"{days} ημέρες"
    
    return difference