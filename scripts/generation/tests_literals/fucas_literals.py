from generation.utilities.create_literal_list import create_literal_list
# pylint: disable=C0301
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
    ret['objective']['no' if results.obj_medication < 9 else 'yes'].append("λήψης της φαρμακευτικής αγωγής")
    ret['objective']['no' if results.obj_telephone < 9 else 'yes'].append("επικοινωνίας με την χρήση τηλεφώνου")
    ret['objective']['no' if results.obj_financial < 9 else 'yes'].append("οικονομικών συναλλαγών")
    ret['objective']['no' if results.obj_hygiene < 9 else 'yes'].append("διατήρησης της προσωπικής υγιεινής")
    ret['objective']['no' if results.obj_orientation < 9 else 'yes'].append("προσανατολισμού/μετακίνησης σε χώρο")
    ret['objective']['no' if results.obj_dressing < 9 else 'yes'].append("ένδυσης")

    ret['examples'] = {
        "κατανόησης": "να κατανοήσει μια πληροφορία/οδηγία όταν είναι σύνθετη και πιθανόν να χρειάζεται να επαναληφθεί", 
        "προοπτικής μνήμης": "να θυμηθεί να κάνει κάτι σε συγκεκριμένο χρόνο (π.χ. να πάρει ένα φάρμακο την συγκεκριμένη ώρα, να κλείσει τον φούρνο, να πάει σε κάποιο προγραμματισμένο ραντεβού)", 
        "σχεδιασμού έργων": "να μπορεί να ορίσει τα βήματα προκειμένου να ολοκληρώσει ένα σύνθετο έργο (να μπορεί να σχεδιάσει ένα ταξίδι, ένα γεύμα για πολλά άτομα, να οργανώσει τις δράσεις μίας ημέρας)", 
        "χρόνου διεκπεραίωσης έργων": "να ολοκληρώνει μία δραστηριότητα σε φυσιολογικό χρόνο", 
        "διαδοχής βημάτων για την διεκπεραίωση έργων": "να ακολουθήσει την σωστή σειρά βημάτων για να ολοκληρώσει ένα έργο", 
        "ακρίβειας βημάτων για την διεκπεραίωση έργων": "να εκτελέσει ορθά (με ακρίβεια) τα βήματα που απαιτούνται για την ολοκλήρωση ενός σύνθετου έργου", 
        "ολοκλήρωσης στόχου": "να ολοκληρώσει ένα σύνθετο έργο χωρίς να χρειαστεί βοήθεια",
    }

    return ret
