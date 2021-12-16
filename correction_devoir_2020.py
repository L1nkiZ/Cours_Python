# 1 Conditionnel

def est_perime(aujoudhui, date_peremption):
  auj_jour, auj_mois, auj_annee = aujoudhui # On n'est pas oblige mais cela evite de passer par les indices
  per_jour, per_mois, per_annee = date_peremption

  return  (auj_annee > per_annee) or (auj_annee == per_annee and auj_mois > per_mois) or (auj_annee == per_annee and auj_mois == per_mois and auj_jour > per_jour)

print(est_perime((1, 1, 2000), (12, 12, 2001)))
print(est_perime((1, 1, 2000), (12, 12, 2000)))
print(est_perime((1, 1, 2000), (1, 12, 2000)))
print(est_perime((12, 12, 2000), (1, 1, 2000)))
print(est_perime((12, 12, 2000), (1, 12, 2000)))
print(est_perime((12, 1, 2000), (1, 1, 2000)))

# 2 Manipulation de tuples

# Question 2

def supprime(t, i):
  res = tuple()

  for j in range(len(t)):
    if i != j:
      res = res + (t[j], )

  return res 

print(supprime((1, 2, 3, 4, 5), -1))
print(supprime((1, 2, 3, 4, 5), 0))
print(supprime((1, 2, 3, 4, 5), 2))
print(supprime((1, 2, 3, 4, 5), 4))
print(supprime((1, 2, 3, 4, 5), 7))

# Question 3

def remplace(t, c1, c2):
  res = tuple()

  for c in t: # on n'a pas besoin de l'indice
    if c == c1:
      res = (c2, ) + res
    else:
      res = (c, ) + res

  return res

print(remplace(('a', 'b', 'c', 'b', 'n'), 'b', 'e'))

# 3 Permutation

# Question 3

# On verifie si chacun des entiers est present
def est_present(liste, valeur):
  for i in liste:
    if valeur == i:
      return True
  
  return False

def est_permut_v1(permutation):
  for i in range(len(permutation)):
    if not est_present(permutation, i): # On pourrait faire un while ici 
      return False

  return True

print(est_permut_v1([0, 1, 2, 4, 3]))
print(est_permut_v1([0, 1, 4, 4, 3]))
print(est_permut_v1([0, 1, 4, -1, 3]))
print(est_permut_v1([0, 1, 4, 7, 3]))

# Une seconde verstion qui fait moins de comparaison
def est_permut_v2(permutation):
  flag = [] # flag[i] == True ssi i est present dans la permutation
  for i in range(len(permutation)):
    flag.append(False)

  for i in permutation:
    if i < 0 or i >= len(permutation) or flag[i]: # ce ne peut pas être une permutation car la valeur n'est pas bonne ou déjà rencontré
      return False
    else:
      flag[i] = True

  # On n'est pas obligé de vérifié que toutes les valeurs dans flag sont à True car si on termine la bouble c'est que toutes les valeurs étaient présentes une seule fois
  return True

print(est_permut_v2([0, 1, 2, 4, 3]))
print(est_permut_v2([0, 1, 4, 4, 3]))
print(est_permut_v2([0, 1, 4, -1, 3]))
print(est_permut_v2([0, 1, 4, 7, 3]))

# Question 5

def permute(positions, chaine):
  res = ""

  for i in positions:
    res = res + chaine[i]

  return res

print(permute([4, 2, 0, 1, 3], "chien"))

# Question 6

def indice(chaine, c):
  for i in range(len(chaine)):
    if chaine[i] == c:
      return i
  
  return len(chaine)

def cherche_permut(s1, s2):
  res = []

  for c in s2:
    res.append(indice(s1, c))

  return res

print(cherche_permut("chien", "niche"))
