# pylint: disable=C0301

def handle_scores(parsed, document):
    """
    Processes and formats various cognitive and psychological test scores from the parsed data 
    and adds them as a paragraph to the provided document.

    Args:
        parsed (dict): A dictionary containing the test scores. The keys are the test names 
                       (e.g., 'mmse', 'ravlt', 'rocft', etc.) and the values are objects with 
                       a 'score' attribute or other relevant attributes.
        document (Document): A document object where the formatted scores will be added as a paragraph.

    Returns:
        None
    """
    totaltxt = ''

    if 'mmse' in parsed and parsed['mmse'].administered:
        totaltxt += f"MMSE: {str(parsed['mmse'].score)}/30\n"
    if 'ravlt' in parsed and parsed['ravlt'].administered:
        totaltxt += f"RAVLT Ικανότητα μάθησης / Ικανότητα συγκράτησης: {str(parsed['ravlt'].l_score)}/{str(parsed['ravlt'].m_score)}/15\n"
    if 'rocft' in parsed and parsed['rocft'].administered:
        totaltxt += f"ROCFT: Αντιγ/Καθυστ.Ανάκλ.: {str(parsed['rocft'].c_score)}/{str(parsed['rocft'].d_score)}/36\n"
    if 'fucas' in parsed and parsed['fucas'].administered:
        totaltxt += f"FUCAS: {str(parsed['fucas'].score)}/126\n"
    if 'frssd' in parsed and parsed['frssd'].administered:
        totaltxt += f"FRSSD: {str(parsed['frssd'].score)}/42\n"
    if 'npi' in parsed and parsed['npi'].administered:
        totaltxt += f"NPI: {str(parsed['npi'].score)}/120\n"
    if 'gds' in parsed and parsed['gds'].administered:
        totaltxt += f"GDS: {str(parsed['gds'].score)}/15\n"
    if 'sast' in parsed and parsed['sast'].administered:
        totaltxt += f"SAST Άγχος: {str(parsed['sast'].score)}/40\n"
    if 'bdi' in parsed and parsed['bdi'].administered:
        totaltxt += f"BDI: {str(parsed['bdi'].score)}/69\n"

    document.add_paragraph(totaltxt)
