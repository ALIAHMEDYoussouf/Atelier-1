def assurance_auto():
    age=float(input("veuillez saisir votre age"))
    permi=float(input("votre anne de permi"))
    accident=float(input("saisir nombre daccident"))
    assurance=float(input("veuillez saisir nombre annee assrance"))
    tarif=''
    if (age<25 and permi<2 and accident==0):
        tarif="rouge"
    elif ():
        tarif="refusé"  
    
    elif(age<25 and permi>=2 or age>=25 and permi<2):
     if(accident==0):
         tarif="orange"
    elif(accident==1):
        tarif="rouge"
    elif():
        tarif="refusée"
    elif(accident==0):
     tarif="vert"     
    elif(accident==1):
        tarif="orange"
    elif(accident==2):
        tarif="rouge"
    elif():
        tarif="refuse"
    if (assurance):
     if(tarif=="rouge"):
         tarif="orange"
    elif(tarif=="orange"):
        tarif="vert"
    elif(tarif=="vert"): 
        tarif="bleu"  

    return tarif
print( assurance_auto () )
