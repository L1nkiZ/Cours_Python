def chiffre_decimal (val):
    if val == 1:
        return ("I")

    if val > 1 and val < 5 :
        chiffre = ""
        for i in range (val):
            chiffre = chiffre + "I"
        return (chiffre)
    if val == 5:
        return ("V")

    if val > 5 and val < 10:
        chiffre ="V"
        val = val - 5
        for i in range (val):
            chiffre = chiffre + "I"
        return chiffre

def chiffre_dizaine(val):
    if val == 10:
        print ("X")

    if val > 10 and val < 50:
        v1 = val//10   
        v2 = val%10       #23 -> 2 * 10 = 23 // 10 % 10 ET 23 % 10 = 3
        chiffred = ""
        for i in range(v1):
            chiffred = chiffred + "X"
        res = chiffred + chiffre_decimal(v2)
        print (res)

    if val == 50:
        print ("L")

    if val > 50 and val < 100:
        v1 = val//50   
        v2 = val%50       #23 -> 2 * 10 = 23 // 10 % 10 ET 23 % 10 = 3
        chiffred = ""
        for i in range(v1):
            chiffred = chiffred + "L"
        res = chiffred + chiffre_decimal(v2)
        print (res)

    else:
        print (chiffre_decimal(val))





chiffre_dizaine(20)
