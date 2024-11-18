def rocft_literals(results, age, education):
    ret = {}

    # delayed_recall_score
    
    # <5 score: σοβαρη

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
    severe = (age >= 50 and age <= 59 and education <= 6 and results.d_score <= 11.5) or \
                (age >= 50 and age <= 59 and education <= 12 and results.d_score <= 14) or \
                (age >= 50 and age <= 59 and education >= 13 and results.d_score <= 15) or \
                (age >= 60 and age <= 69 and education <= 6 and results.d_score <= 11) or \
                (age >= 60 and age <= 69 and education <= 12 and results.d_score <= 12.5) or \
                (age >= 60 and age <= 69 and education >= 13 and results.d_score <= 12.5) or \
                (age >= 70 and education <= 6 and results.d_score <= 11) or \
                (age >= 70 and education <= 12 and results.d_score <= 11.5) or \
                (age >= 70 and education >= 13 and results.d_score <= 11.5)

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
    mild = (age >= 50 and age <= 59 and education <= 6 and results.d_score <= 14.5) or \
                (age >= 50 and age <= 59 and education <= 12 and results.d_score <= 17) or \
                (age >= 50 and age <= 59 and education >= 13 and results.d_score <= 18) or \
                (age >= 60 and age <= 69 and education <= 6 and results.d_score <= 13.5) or \
                (age >= 60 and age <= 69 and education <= 12 and results.d_score <= 15) or \
                (age >= 60 and age <= 69 and education >= 13 and results.d_score <= 16.5) or \
                (age >= 70 and education <= 6 and results.d_score <= 13) or \
                (age >= 70 and education <= 12 and results.d_score <= 13.5) or \
                (age >= 70 and education >= 13 and results.d_score <= 14.5)

    # ++ references at the end

    if severe :
        ret["recall"] = f"παρουσίασε {'σοβαρή' if results.d_score <= 5 else 'σημαντική'} έκπτωση"
        ret["recall_explanation"] = "κατάφερε να ανακαλέσει ελάχιστα στοιχεία"
    elif mild :
        ret["recall"] = "παρουσίασε έκπτωση"
        ret["recall_explanation"] = "δεν κατάφερε να ανακαλέσει σύμφωνα με τα όρια κατωφλίου ικανοποιητικό αριθμό στοιχείων"
    else:
        ret["recall"] = "δεν παρουσίασε έκπτωση"
        ret["recall_explanation"] = "κατάφερε να ανακαλέσει σύμφωνα με τα όρια κατωφλίου ικανοποιητικό αριθμό στοιχείων"

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
    severe_c = (age >= 50 and age <= 59 and education <= 6 and results.c_score <= 28) or \
                (age >= 50 and age <= 59 and education <= 12 and results.c_score <= 28.5) or \
                (age >= 50 and age <= 59 and education >= 13 and results.c_score <= 29) or \
                (age >= 60 and age <= 69 and education <= 6 and results.c_score <= 27) or \
                (age >= 60 and age <= 69 and education <= 12 and results.c_score <= 27) or \
                (age >= 60 and age <= 69 and education >= 13 and results.c_score <= 28.5) or \
                (age >= 70 and education <= 6 and results.c_score <= 24) or \
                (age >= 70 and education <= 12 and results.c_score <= 26.5) or \
                (age >= 70 and education >= 13 and results.c_score <= 26.5)

    # "παρουσίασε έκπτωση"
    # 50-59 & <=6 edu: 28.5
    # 50-59 & <=12 edu: 29.5
    # >=60-69 & 6<=12 edu: 28
    mild_c = (age >= 50 and age <= 59 and education <= 6 and results.c_score <= 28.5) or \
                (age >= 50 and age <= 59 and education <= 12 and results.c_score <= 29.5) or \
                (age >= 60 and age <= 69 and education <= 6 and results.c_score <= 28)
    
    return ret

