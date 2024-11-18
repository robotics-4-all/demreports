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

    mmse = get_children_of_type("MMSE", model)
    if len(mmse) > 0:
        ret['mmse'] = mmse[0]

    ravlt = get_children_of_type("RAVLT", model)
    if len(ravlt) > 0:
        ret['ravlt'] = ravlt[0]

    rocft = get_children_of_type("ROCFT", model)
    if len(rocft) > 0:
        ret['rocft'] = rocft[0]
   
    fucas = get_children_of_type("FUCAS", model)
    if len(fucas) > 0:
        ret['fucas'] = fucas[0]

    frssd = get_children_of_type("FRSSD", model)
    if len(frssd) > 0:
        ret['frssd'] = frssd[0]

    npi = get_children_of_type("NPI", model)
    if len(npi) > 0:
        ret['npi'] = npi[0]

    gds = get_children_of_type("GDS", model)
    if len(gds) > 0:
        ret['gds'] = gds[0]

    sast = get_children_of_type("SAST", model)
    if len(sast) > 0:
        ret['sast'] = sast[0]

    bdi = get_children_of_type("BDI", model)
    if len(bdi) > 0:
        ret['bdi'] = bdi[0]

    return ret