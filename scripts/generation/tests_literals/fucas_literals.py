from generation.utilities.create_literal_list import create_literal_list

def fucas_literals(results):
    """
    Analyzes the given results and categorizes them into various cognitive and functional performance metrics.

    Args:
        results (object): An object containing various attributes related to cognitive and functional performance scores.

    Returns:
        dict: A dictionary containing the following keys:
            - 'global_score' (str): The overall performance score categorized as 'normal', 'minor', or 'severe'.
            - 'individual_affected' (list): A list of strings describing the affected cognitive areas.
            - 'individual_unaffected' (list): A list of strings describing the unaffected cognitive areas.
            - 'affected' (str): A concatenated string of affected cognitive areas.
            - 'unaffected' (str): A concatenated string of unaffected cognitive areas.
            - 'objective' (dict): A dictionary with keys 'no' and 'yes', each containing lists of strings describing the performance in specific objective tasks.
    """
    ret = {}

    # Global score
    if results.score < 44:
        ret['global_score'] = "normal"
    elif results.score < 50:
        ret['global_score'] = "minor"
    else:
        ret['global_score'] = "severe"

    # Epimerous
    ret['individual_affected'] = []
    ret['individual_unaffected'] = []

    lits = {
        "understanding": "κατανόησης", 
        "prospective_memory": "προοπτικής μνήμης", 
        "planning": "σχεδιασμού έργων", 
        "time": "χρόνου διεκπεραίωσης έργων", 
        "sequence": "διαδοχής βημάτων για την διεκπεραίωση έργων", 
        "accuracy": "ακρίβειας βημάτων για την διεκπεραίωση έργων", 
        "goal": "ολοκλήρωσης στόχου",
    }

    for key, value in lits.items():
        category = 'individual_affected' if getattr(results, key) > 1 else 'individual_unaffected'
        ret[category].append(value)

    ret['affected'] = create_literal_list(ret['individual_affected'])
    ret['unaffected'] = create_literal_list(ret['individual_unaffected'])

    ret['objective'] = {
        'no': [],
        'yes': []
    }
    ret['objective']['no' if results.obj_medication < 9 else 'yes'].append(f"λήψης της φαρμακευτικής αγωγής ({results.obj_medication}/27)")
    ret['objective']['no' if results.obj_telephone < 9 else 'yes'].append(f"επικοινωνίας με την χρήση τηλεφώνου ({results.obj_telephone}/27)")
    ret['objective']['no' if results.obj_financial < 9 else 'yes'].append(f"οικονομικών συναλλαγών ({results.obj_financial}/27)")
    ret['objective']['no' if results.obj_hygiene < 9 else 'yes'].append(f"διατήρησης της προσωπικής υγιεινής ({results.obj_hygiene}/27)")
    ret['objective']['no' if results.obj_orientation < 9 else 'yes'].append(f"προσανατολισμού σε χώρο ({results.obj_orientation}/27)")
    ret['objective']['no' if results.obj_dressing < 9 else 'yes'].append(f"ένδυσης ({results.obj_dressing}/27)")

    return ret