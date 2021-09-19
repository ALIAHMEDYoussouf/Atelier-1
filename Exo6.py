def concessionnaire_automobile():
    nb_kilometre=float(input("veuillez saisir le nomvbre de kilometre en une année"))
    carburant=input("veuillez type de carburant")
    cylindre=float(input("veuilllez saisir cylindre"))
    surcoupessence=1.5
    surcoupdiesel=1.7
    prix_essence= 400  # prix essence ce le prix de carburant 
    prix_diesel=200 # prix de diesel de carburant
    if carburant=='e'and cylindre>2000:
        consomation=nb_kilometre*(10/100)
    elif carburant=='e'and cylindre<2000:
        consomation=nb_kilometre*(8/100)   
        prix_anne=(prix_essence*consomation)*surcoupessence

    if carburant=='d'and cylindre>2000:

        consomation=nb_kilometre*(8/100) 
        prix_anne=(prix_diesel*consomation)*surcoupdiesel

    prix_mensuel=prix_anne/12   
    return prix_mensuel

print(concessionnaire_automobile()) 


