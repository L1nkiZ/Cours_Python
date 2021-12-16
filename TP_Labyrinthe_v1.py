def init(nbre_ligne, nbre_colonne):
    res = []
    matrice = []
    for i in range (nbre_ligne):
        if i == 0 or i == nbre_ligne: 
            for j in range(nbre_colonne):
                res = res + ["#",]
        else:
            for k in range(nbre_colonne):
                if k == 0 or k == nbre_colonne:
                    res = res + ["#",]
                else:
                    res = [res] + ["",]
        matrice = matrice + res
    return matrice

def est_vide(labyrinthe, i, j):
    print ("Hey")
    
    
    

print(init(4,5))
            