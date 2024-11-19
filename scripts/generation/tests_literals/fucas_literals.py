from generation.utilities.create_literal_list import create_literal_list

def fucas_literals(results):
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
    if results.understanding > 1:
        ret['individual_affected'].append("κατανόησης")
    else:
        ret['individual_unaffected'].append("κατανόησης")

    if results.prospective_memory > 1:
        ret['individual_affected'].append("προοπτικής μνήμης")
    else:
        ret['individual_unaffected'].append("προοπτικής μνήμης")

    if results.planning > 1:
        ret['individual_affected'].append("σχεδιασμού έργων")
    else:
        ret['individual_unaffected'].append("σχεδιασμού έργων")

    if results.time > 1:
        ret['individual_affected'].append("χρόνου διεκπεραίωσης έργων")
    else:
        ret['individual_unaffected'].append("χρόνου διεκπεραίωσης έργων")

    if results.sequence > 1:
        ret['individual_affected'].append("διαδοχής βημάτων για την διεκπεραίωση έργων")
    else:
        ret['individual_unaffected'].append("διαδοχής βημάτων για την διεκπεραίωση έργων")

    if results.accuracy > 1:
        ret['individual_affected'].append("ακρίβειας βημάτων για την διεκπεραίωση έργων")
    else:
        ret['individual_unaffected'].append("ακρίβειας βημάτων για την διεκπεραίωση έργων")

    if results.goal > 1:
        ret['individual_affected'].append("ολοκλήρωσης στόχου")
    else:
        ret['individual_unaffected'].append("ολοκλήρωσης στόχου")

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
    ret['objective']['no' if results.obj_dressing < 9 else 'yes'].append(f"ένδυσης")

    return ret