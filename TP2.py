#def unités_décimales(chiffre):
#    rep=""
#    if chiffre>=5:
#        rep=rep+"V"
#        chiffre-=5
#    while chiffre>0:
#        chiffre-=1
#        rep=rep+"I"
#    return(rep)


#question 1:

def chiffre_décimal(chiffre,lettre_un,lettre_deux):
    rep=""
    if chiffre>=5:
        rep=rep+lettre_deux
        chiffre-=5
    while chiffre>0:
        chiffre-=1
        rep=rep+lettre_un
    return(rep)


#question 2:

def unités_décimal(chiffre):
    return(chiffre_décimal(chiffre,"I","V"))

#question 3:

def dizaines_décimales(chiffre):
    return(chiffre_décimal(chiffre,"X","L"))

#question 4:

def centaines_décimales(chiffre):
    return(chiffre_décimal(chiffre,"C","D"))

#question 5:

def milliers_décimaux(chiffre):
    return(chiffre_décimal(chiffre,"M",""))

# Assemblage:

def conversion(nombre):
    rep=unités_décimal(nombre%10)
    nombre=nombre//10
    rep=dizaines_décimales(nombre%10)+rep
    nombre=nombre//10
    rep=centaines_décimales(nombre%10)+rep
    nombre=nombre//10
    rep=milliers_décimaux(nombre)+rep
    return(rep)






#question 1:

def chiffre_décimal(chiffre,lettre_un,lettre_deux,lettre_trois):
    if chiffre==9:
        return(lettre_un+lettre_trois)
    rep=""
    if chiffre>=5:
        rep=rep+lettre_deux
        chiffre-=5
    while chiffre>0:
        chiffre-=1
        rep=rep+lettre_un
    return(rep)

#question 2:

def unités_décimal(chiffre):
    return(chiffre_décimal(chiffre,"I","V","X"))


def dizaines_décimales(chiffre):
    return(chiffre_décimal(chiffre,"X","L","C"))


def centaines_décimales(chiffre):
    return(chiffre_décimal(chiffre,"C","D","M"))


def milliers_décimaux(chiffre):
    return(chiffre_décimal(chiffre,"M","",""))

#question 3:

def conversion(nombre):
    rep=unités_décimal(nombre%10)
    nombre=nombre//10
    rep=dizaines_décimales(nombre%10)+rep
    nombre=nombre//10
    rep=centaines_décimales(nombre%10)+rep
    nombre=nombre//10
    rep=milliers_décimaux(nombre)+rep
    return(rep)



