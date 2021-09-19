"""Atelier 1 Exo 1: fonction calcule salaire mensuel d’un employé payé à l’heure 
à partir de son salaire horaire et du nombre d’heures de travail """
def calcule_salaire():
    salaire_Horaire=float (input("veuillez saisir le salaire horaire: "))
    nbr_heur_travail=float(input("veuillez saisir le nombre heur de travail: "))
    salaire_mensuel=0
    taux_horaire=250
    
    heursup25=nbr_heur_travail-160
    heursup50=nbr_heur_travail-200
    horaire_majore25=salaire_Horaire*(heursup25*1.25)
    horaire_majore50=salaire_Horaire*(heursup50*1.5)
    taux_horaire=nbr_heur_travail
    if (taux_horaire<160):
        salaire_mensuel=salaire_Horaire*nbr_heur_travail
    elif (taux_horaire>160):
        salaire_mensuel=salaire_Horaire*nbr_heur_travail+horaire_majore25
    elif (taux_horaire>200):
        salaire_mensuel=salaire_Horaire*nbr_heur_travail+horaire_majore50
    return salaire_mensuel    
res=calcule_salaire()
print("votre heur de travaille est :",res)

    
