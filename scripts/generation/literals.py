from generation.utilities.get_relations_literals import get_relations_literals
from generation.utilities.date_difference import date_difference

def generate_literals(parsed):
    """
    Generates a dictionary of literals based on the parsed patient information.
    """
    ret = {}

    relations = get_relations_literals()
    patient = parsed['patient']
    gender = patient.gender

    # Articles and gender-specific words
    ret["article_caps"] = "Η" if gender == "F" else "Ο"
    ret["article_v2"] = "στην" if gender == "F" else "στον"
    ret["examinee_gender"] = "της εξεταζόμενης" if gender == "F" else "του εξεταζόμενου"
    ret["examinee_gender_v2"] = "στην εξεταζόμενη" if gender == "F" else "στον εξεταζόμενο"
    ret["article_v3"] = "της" if gender == "F" else "του"
    ret["the_same"] = "της ίδιας" if gender == "F" else "του ίδιου"

    # Patient info
    ret["full_name"] = f"{patient.surname} {patient.name}"
    ret["first_name"] = patient.name
    ret["last_name"] = patient.surname
    ret['full_with_article'] = f"{ret['article_caps'].lower()} {ret['full_name']}"
    ret['full_with_article_capital'] = f"{ret['article_caps']} {ret['full_name']}"
    ret["parents_names"] = ""
    if patient.father_name != "" and patient.mother_name != "":
        ret["parents_names"] = f" του {patient.father_name} και της {patient.mother_name},"
    ret["amka"] = f" με ΑΜΚΑ {patient.amka}," if patient.amka != "" else ""

    ret["unit"] = ""
    if patient.unit == "saint helen":
        ret["unit"] = "τη Μονάδα Αντιμετώπισης προβλημάτων Νόσου Alzheimer, «Αγία Ελένη», της Ελληνικής Εταιρείας Νόσου Alzheimer και Συγγενών Διαταραχών, που στεγάζεται στην οδό Πέτρου Συνδίκα 13"

    # Revisit
    ret["revisit"] = patient.revisit
    ret["revisit_date"] = patient.revisit_date
    ret["att_literal_1"] = ""
    ret["att_literal_2"] = ""
    num_atts = patient.att_1_existed + patient.att_2_existed
    if num_atts == 1:
        # We assume that if 1 attenant exists, it is the first one
        ret["att_literal_1"] = "συνοδό"
        ret["att_literal_1"] = ("την " if patient.att_1_gender == "F" else "τον " + ret["att_literal_1"]) + ret["att_literal_1"]
        ret["att_names"] = f"κ. {patient.att_1_name}"
        ret["att_names_with_relations"] = relations[patient.att_1_rel][patient.att_1_gender] + " " + ret["att_names"]
    elif num_atts == 2:
        ret["att_literal_1"] = "τους συνοδούς"
        trimmed_name_1 = patient.att_1_name[:-1] if patient.att_1_gender == "M" else patient.att_1_name
        trimmed_name_2 = patient.att_2_name[:-1] if patient.att_2_gender == "M" else patient.att_2_name
        ret["att_names"] = f"κ. {trimmed_name_1} και κ. {trimmed_name_2}"
        ret["att_names_with_relations"] = relations[patient.att_1_rel][patient.att_1_gender] + " κ. " + patient.att_1_name + " και " + relations[patient.att_2_rel][patient.att_2_gender] + " κ. " + patient.att_2_name
    else:
        ret["att_literal_1"] = "τον ίδιο"
        ret["att_names"] = ""
        ret["att_names_with_relations"] = ""

    if patient.revisit and patient.revisit_date != "":
        ret["revisit_after"] = date_difference(patient.date_med, patient.revisit_date)

    return ret