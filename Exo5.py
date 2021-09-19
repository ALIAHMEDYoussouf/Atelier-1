def calcul_frai_portuaire():
    """"""
    nom=str(input("veuillez saisir votre nom: "))
    longeur=float(input("veuillez saisir votre longeur: "))
    categorie=int(input("veuillez saisir votre categorie du voilier: (1 ou 2 ou 3): "))
  

    if longeur< 5:
        cout_mensuel=100
    elif longeur >=5 and longeur<=10:
        cout_mensuel=200
    elif longeur>10 and longeur<=12:
        cout_mensuel=400
    elif longeur>12:
        cout_mensuel=600
    if categorie==1:
        taxe_special_anuel=100
    elif categorie==2:
        taxe_special_anuel=150
    elif categorie==3:
        taxe_special_anuel=250 
    cout_annuel=cout_mensuel+taxe_special_anuel*12
    return cout_annuel
print("le coût annuel d’une place au port pour le voilier est: ",calcul_frai_portuaire(),'euro')                        
