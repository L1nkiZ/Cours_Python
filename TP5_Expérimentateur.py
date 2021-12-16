from random import randint
import matplotlib.pyplot as plt


def crée_expérience(m, p):
    marqueurs_possibles = [i for i in range(10*m)]
    marqueurs = []
    for i in range(m):
        j = randint(0, len(marqueurs_possibles)-1-i)
        marqueurs.append(marqueurs_possibles[j])
        marqueurs_possibles[j] = marqueurs_possibles[len(
            marqueurs_possibles)-1-i]
    marqueurs.sort()

    marqueurs_positifs = []
    tmp = [i for i in range(m)]
    for i in range(p):
        j = randint(0, m-1-i)
        marqueurs_positifs.append(marqueurs[tmp[j]])
        tmp[j] = tmp[m-1-i]
    marqueurs_positifs.sort()

    return marqueurs, marqueurs_positifs


def comparaison(m):
    res1, res2, res3 = [], [], []

    for p in range(m+1):
        marqueurs, marqueurs_positifs = crée_expérience(m, p)

        mn1, compteur1 = stratégie_1(marqueurs, marqueurs_positifs)
        mn2, compteur2 = stratégie_2(marqueurs, marqueurs_positifs)
        mn3, compteur3 = stratégie_3(marqueurs, marqueurs_positifs)

        res1.append(compteur1)
        res2.append(compteur2)
        res3.append(compteur3)

    abscisse = [i for i in range(m+1)]
    plt.xlabel("p")
    plt.ylabel("Nombre de comparaisons")
    plt.title("m = " + str(m))
    plt.plot(abscisse, res1, label="Stratégie 1")
    plt.plot(abscisse, res2, label="Stratégie 2")
    plt.plot(abscisse, res3, label="Stratégie 3")
    plt.show()


def stratégie_1(marqueurs, marqueurs_positifs):
    return [], 0


def stratégie_2(marqueurs, marqueurs_positifs):
    return [], 0


def stratégie_3(marqueurs, marqueurs_positifs):
    return [], 0


def exécute_comparaison():
    for i in range(10):
        comparaison((i+1)*10)


if __name__ == "__main__":
    exécute_comparaison()
