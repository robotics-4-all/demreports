"""
File that contains the literals for the RAVLT test cases
"""
# pylint: disable=C0301

def ravlt_literals(ravlt_results, age):
    """
    Analyzes RAVLT (Rey Auditory Verbal Learning Test) results and provides a summary of learning and memory retention abilities.
    Parameters:
    ravlt_results (object): An object containing RAVLT scores with attributes `l_score` (learning score) and `m_score` (memory score).
    age (int): The age of the individual being tested.
    Returns:
    dict: A dictionary containing the analysis results with keys:
        - "learning": A string describing the learning ability.
        - "learning_explanation": A string explaining the learning ability result.
        - "maintain": A string describing the memory retention ability.
        - "maintain_explanation": A string explaining the memory retention ability result.
    """
    ret = {}

    # Learning:
    # <70: 8.5, 11.5, ok
    # <80: 6.5, 8.5, ok
    # default: 5.5, 7.5, ok
    # score: 0 --> σοβαρα ελλειμματα
    ls = ravlt_results.l_score
    severe = (age < 70 and ls <= 8.5) or (age < 80 and ls <= 6.5) or ls <= 5.5
    mild = (age < 70 and ls <= 11.5) or (age < 80 and ls <= 8.5) or ls <= 7.5

    ret['apospasmatika'] = " (έστω και αποσπασματικά)" if ravlt_results.l_score <= 3 else ""

    if severe :
        ret["learning"] = f"παρουσίασε {'σοβαρά' if ls == 0 else 'σημαντικά'} ελλείμματα"
        ret["learning_explanation"] = "υπήρχε δυσκολία όσον αφορά την κωδικοποίηση νέων πληροφοριών, και δυσκολία στην χρήση αποτελεσματικών στρατηγικών μάθησης, προκειμένου να γίνει η αποθήκευση στην μακρόχρονη μνήμη"
    elif mild :
        ret["learning"] = "παρουσίασε ελλείμματα"
        ret["learning_explanation"] = "υπήρχε δυσκολία όσον αφορά την κωδικοποίηση νέων πληροφοριών, και δυσκολία στην χρήση αποτελεσματικών στρατηγικών μάθησης, προκειμένου να γίνει η αποθήκευση στην μακρόχρονη μνήμη"
    else:
        ret["learning"] = "δεν παρουσίασε ελλείμματα"
        ret["learning_explanation"] = "δεν υπήρχε δυσκολία όσον αφορά την κωδικοποίηση νέων πληροφοριών, όπως και στην χρήση αποτελεσματικών στρατηγικών μάθησης, προκειμένου να γίνει η αποθήκευση στην μακρόχρονη μνήμη"
    ret["learning_problem"] = severe or mild

    # Maintaining:
    # <70: 5.5, 7.5, ok
    # <80: 3.5, 5.5, ok
    # default: 2.5, 4.5, ok
    # score: 0 --> σοβαρα ελλειμματα
    ms = ravlt_results.m_score
    severe = (age < 70 and ms <= 5.5) or (age < 80 and ms <= 3.5) or ms <= 2.5
    mild = (age < 70 and ms <= 7.5) or (age < 80 and ms <= 5.5) or ms <= 4.5

    if severe :
        ret["maintain"] = f"παρουσίασε {'σοβαρή' if ls == 0 else 'σημαντική'} έκπτωση"
        ret["maintain_explanation"] = "δεν κατάφερε να ανακαλέσει/συγκρατήσει σύμφωνα με τα όρια κατωφλίου, σχεδόν καμία από τις λέξεις για τις οποίες είχε προηγηθεί λεκτική μάθηση"
    elif mild :
        ret["maintain"] = "παρουσίασε έκπτωση"
        ret["maintain_explanation"] = "δεν κατάφερε να ανακαλέσει/συγκρατήσει σύμφωνα με τα όρια κατωφλίου, ικανοποιητικό αριθμό λέξεων για τις οποίες είχε προηγηθεί λεκτική μάθηση"
    else:
        ret["maintain"] = "δεν παρουσίασε έκπτωση"
        ret["maintain_explanation"] = "κατάφερε να ανακαλέσει/συγκρατήσει σύμφωνα με τα όρια κατωφλίου, ικανοποιητικό αριθμό λέξεων για τις οποίες είχε προηγηθεί λεκτική μάθηση"
    ret["maintain_problem"] = severe or mild

    return ret
