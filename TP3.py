#TP3

def est_adn(chaine):
    val = len(chaine)
    bo = True
    for i in range(val):
        if chaine[i] == 'A' or chaine[i] == 'C' or chaine[i] == 'G' or chaine[i] == 'T':
            bo = True
        else:
            bo= False
        if bo == False:
            return bo
    return bo

def transcrit (arn):
    val = len(arn)
    res = ""
    for i in range(val):
        if arn[i] == 'T':
            res = res + ""
            res = res + "U"
        else:
            res = res + arn[i]
    return res

def base_complémentaire(base):
    val = len(base)
    res = ""
    if base == 0:
        return res
    if base == "A":
        res = "T"
    if base == "G":
        res = "C"
    if base == "T":
        res = "A"
    if base == "C":
        res = "G"       
    return res

def séquence_complémentaire_inversée (comp):
    val = len(comp)
    res = ""
    inv = ""
    x = val
    for i in range (val):
        res = res + base_complémentaire(comp[i])
        if i == val-1:
            for j in range(val):
                inv = inv + res[x-1]
                x = x - 1 
    return inv

def nombre_occurrences_codon (codon, sequencearn):
    val = len(sequencearn)
    res = 0
    x = 0
    extrait = ""
    for i in range (val):
        extrait = extrait +sequencearn[i]
        x = x + 1
        if x == 3:
            if codon in extrait:
                res = res + 1
                extrait =""
                x = 0
            else:
                x = 0
                extrait =""

    return res




#print (est_adn(mot))
#print (transcrit(mot))
#print (base_complémentaire("H"))
#print (séquence_complémentaire_inversée(mot))
#print (nombre_occurrences_codon("ACG","GCUACGGAGCUUCGGAGCACGUAG"))

#mot = input("Entrez une séquence ADN :")
#codon = input("Entrez un codon :")
mot = "ACTGGATACTTGGACACTCCGACTTGC"
codon = "ACU"
print("Séquence complémentaire-inversée :",séquence_complémentaire_inversée(mot))
seqarn = print("Séquence ARN :", transcrit(mot))
print ("Le codon ",codon," apparaît ",nombre_occurrences_codon(codon,seqarn),"fois dans la séquence ARN")
