## Εκτελεστικές λειτουργίες

# total score: 42 normal, >=44 minor, >=50 dementia

# epimerous: 1 ok, >=2 not ok

# παρουσίαζε δυσκολίες σε ικανότητες που είναι απαραίτητες προκειμένου να ολοκληρωθεί σωστά η εκτέλεση σύνθετων νοητικών έργων/δραστηριοτήτων --> >2

# extra for prospective_memory + accuracy

## ----------------------------------------

# Καθημερινή λειτουργικότητα ++

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

    ret['affected'] = ""
    ret['unaffected'] = ""
    if len(ret['individual_affected']) > 1:
        ret['affected'] = ", ".join(ret['individual_affected'][:-1]) + " και " + ret['individual_affected'][-1]
    elif len(ret['individual_affected']) == 1:
        ret['affected'] = ret['individual_affected'][0]

    if len(ret['individual_unaffected']) > 1:
        ret['unaffected'] = ", ".join(ret['individual_unaffected'][:-1]) + " και " + ret['individual_unaffected'][-1]
    elif len(ret['individual_unaffected']) == 1:
        ret['unaffected'] = ret['individual_unaffected'][0]

    return ret