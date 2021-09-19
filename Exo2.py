def reconnaitre_caractere():
    """fonction qui lit un caractère puis affiche s'il s'agit d'une lettre minuscule, d'une 
    lettre majuscule, d'un chiffre ou d'un caractère spécial"""
    
    caractere = (input("veuillez saisir un  caractere: ")) #ce pour saisir le caractere choisit
    resultat="" 

    if (caractere >= 'a' and caractere <= 'z'):# caractere compris entre a minuscule et z minuscule
        resultat = "Caractère saisie cest un Lettre minuscule"
    elif (caractere >= 'A' and caractere <= 'Z'):# caractere compris entre A majuscule et z majuscule
        resultat = "Caractère saisie cest un Lettre majuscule"
    elif (caractere >= '0' and caractere <= '9'):# caractere compris entre chiffre 0 et 9 minuscule
        resultat = "Caractère saisie cest un Chiffre"
    elif (ord(caractere) >= 0 and ord(caractere) <= 127):# caractere compris entre  1 et 127 cest un caractere speciaux de table ascii de 128
        resultat = "Caractère saisie cest un Caractère special"
    else:
        resultat = "Caractère saisie dans table Ascii existe pas"
    
    return resultat
print(reconnaitre_caractere())    

