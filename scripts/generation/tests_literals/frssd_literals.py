"""
Function that generates literal descriptions of various attributes based on their severity levels.
"""
# pylint: disable=C0301
from generation.utilities.create_literal_list import create_literal_list

def frssd_literals(results):
    """
    Categorizes and generates literal descriptions of various attributes based on their severity levels.

    Args:
        results (object): An object containing attributes related to various conditions, each with a severity level (0 to 3).

    Returns:
        dict: A dictionary containing categorized attributes and their corresponding literal descriptions. The dictionary has the following keys:
            - "no": List of attributes with severity level 0.
            - "mild": List of attributes with severity level 1.
            - "moderate": List of attributes with severity level 2.
            - "severe": List of attributes with severity level 3.
            - "literals": Dictionary mapping each attribute to its literal description in Greek.
            - "finals": Dictionary containing final literal descriptions for each severity category, formatted as sentences.
    """
    ret = {
        "no": [],
        "mild": [],
        "moderate": [],
        "severe": []
    }

    # attributes list
    attrs = ["nutrition", "dressing", "akrateia", "speech", "sleep", "face_recognition", "hygiene", "name_memory", "episodic_memory", "attention", "confusion", "orientation", "emotional_state", "social_responsiveness"]
    class_scores = {0: "no", 1: "mild", 2: "moderate", 3: "severe"}
    for attr in attrs:
        ret[class_scores[getattr(results, attr)]].append(attr)

    ret["literals"] = {
        "nutrition": f"της διατροφής ({results.nutrition}/3)",
        "dressing": f"της ένδυσης ({results.dressing}/3)",
        "akrateia": f"της συγκράτησης ούρων ({results.akrateia}/3)",
        "speech": f"της ομιλίας ({results.speech}/3)",
        "sleep": f"του ύπνου ({results.sleep}/3)",
        "face_recognition": f"της αναγνώρισης προσώπων ({results.face_recognition}/3)",
        "hygiene": f"της διατήρησης της προσωπικής υγιεινής ({results.hygiene}/3)",
        "name_memory": f"της μνήμης ονομάτων ({results.name_memory}/3)",
        "episodic_memory": f"της μνήμης γεγονότων ({results.episodic_memory}/3)",
        "attention": f"της εγρήγορσης/προσοχής ({results.attention}/3)",
        "confusion": f"της σφαιρικής σύγχυσης ({results.confusion}/3)",
        "orientation": f"του προσανατολισμού σε χώρο και χρόνο ({results.orientation}/3)",
        "emotional_state": f"της συγκινησιακής κατάστασης ({results.emotional_state}/3)",
        "social_responsiveness": f"της κοινωνικής απαντητικότητας ({results.social_responsiveness}/3)",
    }

    ret["finals"] = {
        "no": create_literal_list([ret["literals"][attr] for attr in ret["no"]]),
        "mild": create_literal_list([ret["literals"][attr] for attr in ret["mild"]]),
        "moderate": create_literal_list([ret["literals"][attr] for attr in ret["moderate"]]),
        "severe": create_literal_list([ret["literals"][attr] for attr in ret["severe"]])
    }
    cap_lits = {}
    for i in ["no", "mild", "moderate", "severe"]:
        cap_lits[i] = 'στις ικανότητες' if len(ret[i])>1 else 'στην ικανότητα'

    no_n = len(ret["no"])
    mild_n = len(ret["mild"])
    moderate_n = len(ret["moderate"])
    mild_comma = ', ' if no_n > 0 else ''
    moderate_comma = ', ' if mild_n > 0 or no_n > 0 else ''
    severe_comma = ', και ' if moderate_n > 0 or mild_n > 0 or no_n > 0 else ''

    ret["finals"]["no"] = f"δεν αναφέρθηκαν δυσκολίες {cap_lits['no']} " + ret["finals"]["no"] if len(ret["no"]) > 0 else ""
    ret["finals"]["mild"] = f"{mild_comma}αναφέρθηκαν ήπιες δυσκολίες {cap_lits['mild']} " + ret["finals"]["mild"] if len(ret["mild"]) > 0 else ""
    ret["finals"]["moderate"] = f"{moderate_comma}αναφέρθηκαν μέτριες δυσκολίες {cap_lits['moderate']} " + ret["finals"]["moderate"] if len(ret["moderate"]) > 0 else ""
    ret["finals"]["severe"] = f"{severe_comma}αναφέρθηκαν σοβαρές δυσκολίες {cap_lits['severe']} " + ret["finals"]["severe"] if len(ret["severe"]) > 0 else ""

    return ret
