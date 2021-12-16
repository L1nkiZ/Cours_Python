def choix_pivot (liste, ind1, ind2):
    taille = (ind1 + ind2 -1 )//2
    chiffre1 = liste[ind1]
    chiffre2 = liste[ind2-1]
    chiffre3 = liste[taille]
    if (chiffre1 >= chiffre3) == (chiffre3 > chiffre2):
        return taille
    if (chiffre1 <= chiffre2) == (chiffre2 < chiffre3):
        return [ind2-1]
    return ind1


l = [1, 5, 4, 5, 6, 7, 8, 9, 10]
print(choix_pivot(l,0,9))