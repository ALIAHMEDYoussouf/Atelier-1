def impot():
    """une fonction pour savoir si un habitant Zorglub est imposable ou non"""
    imposable=False
    
    sexe=input("veuillez saisir le sexe homme ou femme: ")# demande utilistateur saisir son sexe Homme ou Femme 
    age=int(input("veuillez saisir votre age: "))# demande utilistateur saisir son age
    if sexe=='homme' and age>20:
        imposable=True
    elif (sexe=='femme' and age>=18 and age<=35):
        imposable=True     
    else:
        imposable=False
    return imposable  
print(impot())          