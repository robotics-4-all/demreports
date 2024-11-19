"""
File containing the literals for the ROCFT test cases
"""
# pylint: disable=C0301

def rocft_literals(results, age, education):
    """
    Evaluates the recall and copy scores based on age and education levels and returns a dictionary with the results.
    Parameters:
    results (object): An object containing the scores `d_score` (delayed recall score) and `c_score` (copy score).
    age (int): The age of the individual.
    education (int): The number of years of education the individual has completed.
    Returns:
    dict: A dictionary containing the evaluation of recall and copy scores with keys:
        - "recall": A string indicating the level of recall impairment.
        - "recall_explanation": A string explaining the recall impairment.
    """
    ret = {}

    # delayed_recall_score

    # <5 score: σοβαρη
    combos = {
        '50-59-6': age >= 50 and age <= 59 and education <= 6,
        '50-59-12': age >= 50 and age <= 59 and education <= 12,
        '50-59-13': age >= 50 and age <= 59 and education >= 13,
        '60-69-6': age >= 60 and age <= 69 and education <= 6,
        '60-69-12': age >= 60 and age <= 69 and education <= 12,
        '60-69-13': age >= 60 and age <= 69 and education >= 13,
        '70-6': age >= 70 and education <= 6,
        '70-12': age >= 70 and education <= 12,
        '70-13': age >= 70 and education >= 13,
    }

    # "παρουσίασε σημαντική έκπτωση"
    # 50-59 & <=6 edu: 11.5
    # 50-59 & <=12 edu: 14
    # 50-59 & >=13 edu: 15
    # 60-69 & <=6 edu: 11
    # 60-69 & <=12 edu: 12.5
    # 60-69 & >=13 edu: 12.5
    # >=70 & <=6 edu: 11
    # >=70 & <=12 edu: 11.5
    # >=70 & >=13 edu: 11.5
    severe_flags_d_score = [
        combos['50-59-6'] and results.d_score <= 11.5, 
        combos['50-59-12'] and results.d_score <= 14,
        combos['50-59-13'] and results.d_score <= 15,
        combos['60-69-6'] and results.d_score <= 11,
        combos['60-69-12'] and results.d_score <= 12.5,
        combos['60-69-13'] and results.d_score <= 12.5,
        combos['70-6'] and results.d_score <= 11,
        combos['70-12'] and results.d_score <= 11.5,
        combos['70-13'] and results.d_score <= 11.5,
    ]
    severe = any(severe_flags_d_score)

    # "παρουσίασε έκπτωση"
    # 50-59 & <=6 edu: 14.5
    # 50-59 & <=12 edu: 17
    # 50-59 & >=13 edu: 18
    # 60-69 & <=6 edu: 13.5
    # 60-69 & <=12 edu: 15
    # 60-69 & >=13 edu: 16.5
    # >=70 & <=6 edu: 13
    # >=70 & <=12 edu: 13.5
    # >=70 & >=13 edu: 14.5
    mild_flags = [
        combos['50-59-6'] and results.d_score <= 14.5,
        combos['50-59-12'] and results.d_score <= 17,
        combos['50-59-13'] and results.d_score <= 18,
        combos['60-69-6'] and results.d_score <= 13.5,
        combos['60-69-12'] and results.d_score <= 15,
        combos['60-69-13'] and results.d_score <= 16.5,
        combos['70-6'] and results.d_score <= 13,
        combos['70-12'] and results.d_score <= 13.5,
        combos['70-13'] and results.d_score <= 14.5,
    ]
    mild = any(mild_flags)

    if severe :
        ret["recall"] = f"παρουσίασε {'σοβαρή' if results.d_score <= 5 else 'σημαντική'} έκπτωση ({results.d_score}/36)"
        ret["recall_explanation"] = "κατάφερε να ανακαλέσει ελάχιστα στοιχεία"
        ret["recall_problem"] = True
    elif mild :
        ret["recall"] = f"παρουσίασε έκπτωση ({results.d_score}/36)"
        ret["recall_explanation"] = "δεν κατάφερε να ανακαλέσει σύμφωνα με τα όρια κατωφλίου ικανοποιητικό αριθμό στοιχείων"
        ret["recall_problem"] = True
    else:
        ret["recall"] = f"δεν παρουσίασε έκπτωση ({results.d_score}/36)"
        ret["recall_explanation"] = "κατάφερε να ανακαλέσει σύμφωνα με τα όρια κατωφλίου ικανοποιητικό αριθμό στοιχείων"
        ret["recall_problem"] = False

    # copy_score

    # "παρουσίασε σημαντική έκπτωση"
    # 50-59 & <=6 edu: 28
    # 50-59 & <=12 edu: 28.5
    # 50-59 & >=13 edu: 29
    # 60-69 & <=6 edu: 27
    # 60-69 & <=12 edu: 27
    # 60-69 & >=13 edu: 28.5
    # >=70 & <=6 edu: 24
    # >=70 & <=12 edu: 26.5
    # >=70 & >=13 edu: 26.5
    severe_flags_c_score = [
        combos['50-59-6'] and results.c_score <= 28,
        combos['50-59-12'] and results.c_score <= 28.5,
        combos['50-59-13'] and results.c_score <= 29,
        combos['60-69-6'] and results.c_score <= 27,
        combos['60-69-12'] and results.c_score <= 27,
        combos['60-69-13'] and results.c_score <= 28.5,
        combos['70-6'] and results.c_score <= 24,
        combos['70-12'] and results.c_score <= 26.5,
        combos['70-13'] and results.c_score <= 26.5,
    ]
    severe_c = any(severe_flags_c_score)

    # "παρουσίασε έκπτωση"
    # 50-59 & <=6 edu: 28.5
    # 50-59 & <=12 edu: 29.5
    # >=60-69 & 6<=12 edu: 28
    mild_flags_c_score = [
        combos['50-59-6'] and results.c_score <= 28.5,
        combos['50-59-12'] and results.c_score <= 29.5,
        combos['60-69-6'] and results.c_score <= 28,
    ]
    mild_c = any(mild_flags_c_score)

    ret["copy_problem"] = severe_c or mild_c

    return ret
