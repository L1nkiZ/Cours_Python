def init(nbre_ligne, nbre_colonne):
    res = []
    matrice = []
    for i in range(nbre_ligne): 
        ligne = []
        if i == 0 or i == nbre_ligne:
            for j in range(nbre_colonne): 
                ligne.append(False)
            matrice.append(ligne) 
        else:
            for k in range(nbre_colonne): 
                ligne.append(False)
            matrice.append(ligne) 
        res = res + matrice
    return (res)

def est_vide(labyrinthe, i, j):
    if labyrinthe [i] [j] == True:
        return True
    else:
        return False


labyrinthe = init(4,5)
print (labyrinthe)
print (est_vide (labyrinthe, 3, 2))
