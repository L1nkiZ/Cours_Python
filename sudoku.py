import parser
import render
from math import sqrt


def is_digit(char):
    return char >= '0' and char <= '9'


def is_number(string):
    first = True

    for c in string:
        if not (c == '-' and first) and not is_digit(c):
            return False
        first = False

    return True


def count_free_cells(grid):
    nb_free_cells = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j][0]:
                nb_free_cells = nb_free_cells + 1

    return nb_free_cells

def empty_grid(dim):
    grid = list()

    for i in range(dim**2):
        ligne = list()
        for j in range(dim**2):
            ligne.append((True, 0))
        grid.append(ligne)

    return grid


def initial_grid(filename):
    dim, values = parser.read(filename)

    grid = empty_grid(dim)

    for i, j, value in values:
        grid[i][j] = (False, value)

    return grid


def draw(grid):
    dim = int(sqrt(len(grid)))

    render.draw_sudoku_grid(dim)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not grid[i][j][0]:
                color = "red"
                value = grid[i][j][1]
            elif grid[i][j][1] == 0:
                color = "green"
                value = "?"
            else:
                color = "blue"
                value = grid[i][j][1]

            render.write(i, j, value, color)


def possible_values_row(row, grid):
    result = list()
    for i in range(len(grid)+1):
        result.append(True)

    for status, i in grid[row]:
        if i != 0:
            result[i] = False

    return result


def possible_values_column(column, grid):
    result = list()
    for i in range(len(grid)+1):
        result.append(True)

    for i in range(len(grid)):
        if grid[i][column][1] != 0:
            result[grid[i][column][1]] = False

    return result


def possible_values_block(row, column, grid):
    result = list()
    for i in range(len(grid)+1):
        result.append(True)

    dim = int(sqrt(len(grid)))

    from_row = (row // dim)*dim
    from_column = (column // dim)*dim

    for i in range(from_row, from_row+dim):
        for j in range(from_column, from_column+dim):
            if grid[i][j][1] != 0:
                result[grid[i][j][1]] = False

    return result


def possible_values(row, column, grid):
    possible_row = possible_values_row(row, grid)
    possible_column = possible_values_column(column, grid)
    possible_block = possible_values_block(row, column, grid)

    self_value = grid[row][column][1]
    possible_row[self_value] = True
    possible_column[self_value] = True
    possible_block[self_value] = True

    result = list()

    for i in range(len(grid)+1):
        if possible_row[i] and possible_column[i] and possible_block[i]:
            result.append(i)

    return result


def input_row(grid):
    correct = False
    ok, row = False, len(grid)

    while not correct:
        row_str = input('Entrez un numéro de ligne ou entrée pour annuler : ')
        if len(row_str) == 0:
            correct = True
        elif not is_number(row_str):
            print("Il faut entrer un nombre entier")
        else:
            row = int(row_str)
            if row < 0 or row >= len(grid):
                print(
                    "Le numéro de ligne n'est pas correct. Il doit être entre 0 et", len(grid)-1)
            else:
                ok, correct = True, True

    return ok, row


def input_column(grid):
    correct = False
    ok, column = False, len(grid)


    while not correct:
        column_str = input('Entre un numéro de colonnes ou entrée pour annuler : ')

        if len(column_str) == 0:
            correct = True
        elif not is_number(column_str):
            print("Il faut entrer un nombre entier")
        else:
            column = int(column_str)
            if column < 0 or column >= len(grid[0]):
                print("Le numéro de colonne n'est pas correct. Il doit être entre 0 et", len(
                    grid[0])-1)
            else:
                ok, correct = True, True

    return ok, column


def input_row_column(grid):
    correct = False
    ok, row, column = False, len(grid), len(grid[0])

    while not correct:
        ok, row = input_row(grid)

        if ok:
            ok, column = input_column(grid)

            if ok and not grid[row][column][0]:
                print("Il n'est pas possible de modifier cette case")
            else:
                correct = True
        else:
            correct = True

    return ok, row, column


# On pourrait faire une recherche dichotomique
def present(sequence, element):
    for e in sequence:
        if e == element:
            return True
    return False


def input_value(possibilities):
    correct = False
    ok, value = False, 0

    print('Les valeurs possibles sont : ', end='')
    for e in possibilities:
        print(e, end=' ')
    print()

    while not correct:
        ui = input(
            'Entrez une valeur possible ou appuyez sur entrée pour annuler le coup : ')

        if not is_number(ui):
            print("Il faut entrer un entier")
        elif len(ui) == 0:
            correct = True
        elif not present(possibilities, int(ui)):
            print("Ce n'est pas une valeur possible")
        else:
            ok, value = True, int(ui)
            correct = True

    return ok, value


def ask_rewind(history):
    ok, row, column, value = False, -1, -1, -1

    if len(history) > 0:
        row, column, previous_value, current_value = history[len(history)-1]
        print('Dernier coup joué = (', row, ',', column, ') :', previous_value, '->', current_value)
        
        correct = False
        while not correct:
            ui = input("Voulez-vous l'annuler ? [O]ui / [N]on : ")
            if ui != 'O' and ui != 'N':
                print("Veuillez répondre 'O' ou 'N'")
            elif ui == 'O':
                correct, ok, value = True, True, previous_value
            else:
                correct = True

    return ok, row, column, value


def next(grid, history):
    rewind = True
    ok, row, column, value = ask_rewind(history)

    if not ok: # l'utilisateur n'a pas pu ou n'a pas voulu annuler coup précédent
        rewind = False # on cherche a jouer un nouveau coup
        ok, row, column = input_row_column(grid)

        if ok:
            ok, value = input_value(possible_values(row, column, grid))

    return ok, row, column, value, rewind


def update(grid, history, row, column, value, rewind, nb_free_cells):
    if value == 0:
        render.write(row, column, "?", "green")
        nb_free_cells = nb_free_cells + 1
    else:
        render.write(row, column, value, "blue")
        nb_free_cells = nb_free_cells - 1

    if not rewind:
        history.append((row, column, grid[row][column][1], value))
    else:
        history.pop()

    grid[row][column] = (True, value)

    return nb_free_cells


def play(grid):
    history = list()

    nb_free_cells = count_free_cells(grid)

    while nb_free_cells > 0:
        print('Il reste', nb_free_cells, 'cases à remplir')

        ok, row, column, value, rewind = next(grid, history)

        if ok and grid[row][column][1] != value: # on joue et il y a un changement
            nb_free_cells = update(grid, history, row, column, value, rewind, nb_free_cells)
            
    print('Félicitation !')


def search_freecells(grid):
    freecells = list()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j][1] == 0:
                freecells.append((i, j))

    return freecells


def forecast(grid, freecells):
    """
    Check if for each cell in freecells, there are still possibilities
    """   
    for row, column in freecells:
        if len(possible_values(row, column, grid)) == 1: # il y a toujours au moins 0
            return False
    
    return True


def solve_recursive(grid, freecells):
    if len(freecells) > 0: # On a reussi fixer toutes les cellules
        cell = freecells[len(freecells)-1] # On prend la dernière cellule
        row, column = cell

        possibilities = possible_values(row, column, grid)

        if len(possibilities) > 0: 
            freecells.pop() # On retire la cellule courante

            for i in range(1, len(possibilities)): # On ne prend pas en compte la valeur 0
                grid[row][column] = (True, possibilities[i])
                render.write(row, column, possibilities[i], "blue")

                # On fait l'appel recursif s'il renvoie true, on s'arrête car la grille a été remplie
                if forecast(grid, freecells) and solve_recursive(grid, freecells):
                    return True

            # Si on est ici c'est qu'aucune valeur n'a marché
            # On remet la cellule comme libre et on retourne faux
            grid[row][column] = (True, 0)
            render.write(row, column, "?", "green")
            freecells.append(cell)

            return False
        else: # Il n'y a pas de possibilité pour cell, il faut backtracker
            return False
    else:
        return True


def solve(grid):
    freecells = search_freecells(grid)
    solve_recursive(grid, freecells)

def open():
    filename = input('Entrez le nom du fichier (entrée pour prendre le fichier par défaut): ')
    if len(filename) == 0:
        grid = initial_grid('sudoku_9_9_1.txt')
    else:
        grid = initial_grid(filename)

    return grid


def ask_play_or_solve():
    correct, answer = False, ""

    while not correct:
        answer = input('Voulez-vous "Jouer" ou "Résoudre" ? ')

        if answer != "Jouer" and answer != "Résoudre":
            print('Il faut répondre "Jouer" ou "Résoudre"')
        else: 
            correct = True

    return answer

if __name__ == "__main__":
    grid = open()
    draw(grid)

    if ask_play_or_solve() == "Jouer":
        play(grid)
    else:
        solve(grid)
    
    render.wait_quit()
