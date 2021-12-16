# Question 1

ref_an = 1900
ref_mois = 1
ref_jour = 1

# Question 2

nbre_sec_jour = 60 * 60 * 24

# Question 3

nbre_sec_an = nbre_sec_jour * 365.2425

# Question 4

nbre_sec_mois = nbre_sec_an / 12

# Question 5

aujourdhui_an = 2021
aujourdhui_mois = 9
aujourdhui_jour = 24

# Question 6

nbre_sec_aujourdhui = (aujourdhui_an - ref_an) * nbre_sec_an
nbre_sec_aujourdhui += (aujourdhui_mois - ref_mois) * nbre_sec_mois
nbre_sec_aujourdhui += (aujourdhui_jour - ref_jour) * nbre_sec_jour

# Question 7

naissance_an = 1945
naissance_mois = 12
naissance_jour = 18

# Question 8

nbre_sec_naissance = (naissance_an - ref_an) * nbre_sec_an
nbre_sec_naissance += (naissance_mois - ref_mois) * nbre_sec_mois
nbre_sec_naissance += (naissance_jour - ref_jour) * nbre_sec_jour

# Question 9

age_en_seconde = nbre_sec_aujourdhui - nbre_sec_naissance

print("L'âge en seconde est", age_en_seconde)
