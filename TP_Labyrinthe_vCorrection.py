from random import randint


def ligne_pleine(nbre_colonnes):
    # ligne = [False] * nbre_colonnes
    ligne = []
    for i in range(nbre_colonnes):                  
        ligne.append(False)
    return ligne


def ligne_vide(nbre_colonnes):
    ligne = [False]
    for i in range(nbre_colonnes-2):
        ligne.append(True)
    ligne.append(False)
    return ligne


def init(nbre_lignes, nbre_colonnes):
    labyrinthe = []

    labyrinthe.append(ligne_pleine(nbre_colonnes))
    for i in range(nbre_lignes-2):
        labyrinthe.append(ligne_vide(nbre_colonnes))
    labyrinthe.append(ligne_pleine(nbre_colonnes))

    return labyrinthe


def est_vide(labyrinthe, i, j):
    return labyrinthe[i][j]


def est_mur(labyrinthe, i, j):
    return not est_vide(labyrinthe, i, j)


def affichage(labyrinthe):
    for i in range(len(labyrinthe)):
        for j in range(len(labyrinthe[i])):
            if est_vide(labyrinthe, i, j):
                print(" ", end='')
            else:
                print("#", end='')
        print()


def place_ilots(labyrinthe, nbre_ilots):
    for i in range(nbre_ilots):
        ligne = randint(1, len(labyrinthe)-2)
        colonne = randint(1, len(labyrinthe[ligne])-2)
        labyrinthe[ligne][colonne] = False


def cas_1(l, i, j):
    return est_vide(l, i-1, j-1) and est_vide(l, i-1, j) and est_vide(l, i, j-1) and est_mur(l, i, j+1) and est_vide(l, i+1, j-1) and est_vide(l, i+1, j)


def cas_2(l, i, j):
    return est_mur(l, i-1, j) and est_vide(l, i, j-1) and est_vide(l, i, j+1) and est_vide(l, i+1, j-1) and est_vide(l, i+1, j) and est_vide(l, i+1, j+1)


def cas_3(l, i, j):
    return est_vide(l, i-1, j) and est_vide(l, i-1, j+1) and est_mur(l, i, j-1) and est_vide(l, i, j+1) and est_vide(l, i+1, j) and est_vide(l, i+1, j+1)


def cas_4(l, i, j):
    return est_vide(l, i-1, j-1) and est_vide(l, i-1, j) and est_vide(l, i-1, j+1) and est_vide(l, i, j-1) and est_vide(l, i, j+1) and est_mur(l, i, j+1)


def est_constructible(labyrinthe, i, j):
    return est_vide(labyrinthe, i, j) and (cas_1(labyrinthe, i, j) or cas_2(labyrinthe, i, j) or cas_3(labyrinthe, i, j) or cas_4(labyrinthe, i, j))


def cases_constructibles(labyrinthe):
    résultat = []

    for i in range(1, len(labyrinthe)-1):
        for j in range(1, len(labyrinthe[i])-1):
            if est_constructible(labyrinthe, i, j):
                résultat.append((i, j))

    return résultat


def générer_labyrinthe(nbre_lignes, nbre_colonnes, nbre_ilots):
    labyrinthe = init(nbre_lignes, nbre_colonnes)
    place_ilots(labyrinthe, nbre_ilots)

    cases_possibles = cases_constructibles(labyrinthe)
    while len(cases_possibles) != 0:
        indice = randint(0, len(cases_possibles)-1)
        #ligne, colonne = cases_possibles[indice][0], cases_possibles[indice][1]
        ligne, colonne = cases_possibles[indice]
        labyrinthe[ligne][colonne] = False
        cases_possibles = cases_constructibles(labyrinthe)

    return labyrinthe


labyrinthe = générer_labyrinthe(6, 10, 5)
affichage(labyrinthe)
