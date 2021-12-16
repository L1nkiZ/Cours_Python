import math

def résoudre (a, b, c):
    if a == 0 and b == 0 and c == 0:
        return("Il y à une infinité de solutions")
    if a == 0 and b == 0 :
        return("Il n'y à pas de solutions")
    if a == 0:
        x = -(c / b)
        return x
    else:
        disc = b * b - 4 *(a * c)
        if disc == 0:
            x = -(b / (2 * a))
            return x
        if disc > 0 :
            x_1 = (-b + math.sqrt(disc) ) / ( 2 *a)
            x_2 = (-b - math.sqrt(disc) ) / ( 2 *a)   
            return x_1, x_2
        if disc < 0 :
            x_1 = (-b + math.sqrt(disc) ) / ( 2 *a)
            x_2 = (-b - math.sqrt(disc) ) / ( 2 *a)   
            return x_1,"i", x_2,"i"

résoudre(0,0,0)