def election_legislative():
    a=float(input("entrer score 1"))
    b=float(input("entrer score 2"))
    c=float(input("entrer score 3"))
    d=float(input("entrer score 4"))
    if (a>50):
        print("elut premier tour") 

    elif(b>50 or c>50 or d>50 or not a>=12.5):

     print("battu")
    elif(a>b and a>=c and a>=d ): 
        print("favorable")
    else :
        print("defavorable")   
        return a
print(election_legislative())       