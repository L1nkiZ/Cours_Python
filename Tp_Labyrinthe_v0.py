matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print("Ligne 0 Colonne 0 =", matrice[0][0])
#print("Ligne 1 Colonne 2 =", matrice[1][2])

matrice = [] # On commence par une matrice vide
for i in range(3): # On construit les lignes une à une
    ligne = [] # On commence par une ligne vide
    for j in range(3): # On construit la ligne
        ligne.append(j+1)
    matrice.append(ligne) # On ajoute la ligne à la matrice

print (matrice)



def affichage(labyrinthe):
    tup1 = ('h','e','l','l','o')

    str = ''

#    Use for loop to convert tuple to string.
    for item in tup1:
       str = str + item

print(str)