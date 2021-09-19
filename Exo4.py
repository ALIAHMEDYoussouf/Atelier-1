def reprographie():
    """fonction qui demande à l’utilisateur le nombre de photocopies effectuées et qui 
    affiche la facture correspondante"""
    nb_photocopie=int(input("veuillez saisir le nombre de photocopie effectue: "))
    facture=0
    t1=0.10# 3 prix t1, t2,t3 
    t2=0.09
    t3=0.08
    p1=10 # deux condition interval inferieur ou egal 10 pour 10 suivant de photocopie et 20 suivant de photocopie 
    p2=30
    if nb_photocopie<=10:
        facture=nb_photocopie*0.10
    elif nb_photocopie>10 and nb_photocopie<=30:
        facture=(p1*t1)+(nb_photocopie-p1)*0.09
    elif nb_photocopie>30:
        facture=(p1*t1)+(p2-p1)*t2+(nb_photocopie-30)*0.08 
    return facture
print(reprographie())            
