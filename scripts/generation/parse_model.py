# pylint: disable=C0301

from textx import get_children_of_type

def parse_model(model):
    """
    Parses the given model to extract various types of information.
    The function looks for specific types of information within the model and 
    returns a dictionary containing the first instance of each type found. 
    If multiple instances of "ReportInfo" or "PatientInfo" are found, the 
    function prints an error message and exits.
    Args:
        model (object): The model to be parsed.
    Returns:
        dict: A dictionary containing the extracted information. The keys 
        are the types of information (e.g., 'report', 'patient', 'mmse', 
        'ravlt', 'rocft', 'fucas', 'frssd', 'npi', 'gds', 'sast', 'bdi') 
        and the values are the corresponding instances found in the model.
    Raises:
        SystemExit: If multiple instances of "ReportInfo" or "PatientInfo" 
        are found in the model.
    """
    ret = {}

    reports = get_children_of_type("ReportInfo", model)
    if len(reports) > 1:
        print("Multiple reports found")
        exit(1)
    ret['report'] = reports[0]

    patient = get_children_of_type("PatientInfo", model)
    if len(patient) > 1:
        print("Multiple patients found")
        exit(1)
    ret['patient'] = patient[0]

    tests_dic = {
        "MMSE": "mmse",
        "RAVLT": "ravlt",
        "ROCFT": "rocft",
        "FUCAS": "fucas",
        "FRSSD": "frssd",
        "NPI": "npi",
        "GDS": "gds",
        "SAST": "sast",
        "BDI": "bdi",
        "BAI": "bai",
    }
    for test, key in tests_dic.items():
        test = get_children_of_type(test, model)
        if len(test) > 0:
            ret[key] = test[0]

    return ret
