import random
import time


def table(l1):
    print("-------------")
    print("|", l1[0][0], "|", l1[0][1], "|", l1[0][2], "|")
    print("-------------")
    print("|", l1[1][0], "|", l1[1][1], "|", l1[1][2], "|")
    print("-------------")
    print("|", l1[2][0], "|", l1[2][1], "|", l1[2][2], "|")
    print("-------------")


def the_end(l1, symbol):
    return l1[0] == [symbol, symbol, symbol] or l1[1] == [symbol, symbol, symbol] or l1[2] == [symbol, symbol, symbol] or (l1[0][0] == symbol and l1[1][0] == symbol and l1[2][0] == symbol) or (l1[0][1] == symbol and l1[1][1] == symbol and l1[2][1] == symbol) or (l1[0][2] == symbol and l1[1][2] == symbol and l1[2][2] == symbol) or (l1[0][0] == symbol and l1[1][1] == symbol and l1[2][2] == symbol) or (l1[0][2] == symbol and l1[1][1] == symbol and l1[2][0] == symbol)


def winer_draw(symbol):
    print(f"{symbol}  is winner !!!")
    return symbol


def end(l1):
    if the_end(l1, x):
        return winer_draw(x)
    elif the_end(l1, o):
        return winer_draw(o)


# def male(symbol, lastCar):
#     if lastCar:
#         print(symbol[0], "je pobjedila: ", symbol[2])
#     else:
#         print(symbol[0], "je pobjedio: ", symbol[2])


def input_row(symbol):
    while True:
        try:
            row, column = input(
                f"{symbol[0]} enter the row and column {symbol[1]} (1,1): ").split(",")
        except:
            continue
        if row.isnumeric() == False or column.isnumeric() == False:
            print("You did not enter a number. ")
            continue
        row = int(row) - 1
        column = int(column) - 1
        if row < 0 or row > 2 or column < 0 or column > 2:
            print(
                "You entered too many or too few numbers. Numbers must be between 1 and 3.")
            continue
        if l1[row][column] != p:
            print("That place is occupied!")
            continue
        l1[row][column] = symbol[1]
        return l1


def compPlay(l1, symbol, symbol2):
    print("Comp play")
    time.sleep(1)
    while True:
        if l1[1][1] == p:
            l1[1][1] = symbol
            return l1
        if comp_hard == True:
            for i in range(0, 3):
                if l1[i] == [symbol, symbol, p]:
                    l1[i][2] = symbol
                    return l1
                elif l1[i] == [symbol, p, symbol]:
                    l1[i][1] = symbol
                    return l1
                elif l1[i] == [p, symbol, symbol]:
                    l1[i][0] = symbol
                    return l1
                elif l1[0][i] == symbol and l1[1][i] == symbol and l1[2][i] == p:
                    l1[2][i] = symbol
                    return l1
                elif l1[0][i] == symbol and l1[1][i] == p and l1[2][i] == symbol:
                    l1[1][i] = symbol
                    return l1
                elif l1[0][i] == p and l1[1][i] == symbol and l1[2][i] == symbol:
                    l1[0][i] = symbol
                    return l1
            if l1[0][0] == p and l1[1][1] == symbol and l1[2][2] == symbol:
                l1[0][0] = symbol
                return l1
            elif l1[0][0] == symbol and l1[1][1] == p and l1[2][2] == symbol:
                l1[1][1] = symbol
                return l1
            elif l1[0][0] == symbol and l1[1][1] == symbol and l1[2][2] == p:
                l1[2][2] = symbol
                return l1

            if l1[0][2] == p and l1[1][1] == symbol and l1[2][0] == symbol:
                l1[0][2] = symbol
                return l1
            elif l1[0][2] == symbol and l1[1][1] == p and l1[2][0] == symbol:
                l1[1][1] = symbol
                return l1
            elif l1[0][2] == symbol and l1[1][1] == symbol and l1[2][0] == p:
                l1[2][0] = symbol
                return l1

            for i in range(0, 3):
                if l1[i] == [symbol2, symbol2, p]:
                    l1[i][2] = symbol
                    return l1
                elif l1[i] == [symbol2, p, symbol2]:
                    l1[i][1] = symbol
                    return l1
                elif l1[i] == [p, symbol2, symbol2]:
                    l1[i][0] = symbol
                    return l1

                elif l1[0][i] == symbol2 and l1[1][i] == symbol2 and l1[2][i] == p:
                    l1[2][i] = symbol
                    return l1
                elif l1[0][i] == symbol2 and l1[1][i] == p and l1[2][i] == symbol2:
                    l1[1][i] = symbol
                    return l1
                elif l1[0][i] == p and l1[1][i] == symbol2 and l1[2][i] == symbol2:
                    l1[0][i] = symbol
                    return l1

            if l1[0][0] == p and l1[1][1] == symbol2 and l1[2][2] == symbol2:
                l1[0][0] = symbol
                return l1
            elif l1[0][0] == symbol2 and l1[1][1] == p and l1[2][2] == symbol2:
                l1[1][1] = symbol
                return l1
            elif l1[0][0] == symbol2 and l1[1][1] == symbol2 and l1[2][2] == p:
                l1[2][2] = symbol
                return l1

            if l1[0][2] == p and l1[1][1] == symbol2 and l1[2][0] == symbol2:
                l1[0][2] = symbol
                return l1
            elif l1[0][2] == symbol2 and l1[1][1] == p and l1[2][0] == symbol2:
                l1[1][1] = symbol
                return l1
            elif l1[0][2] == symbol2 and l1[1][1] == symbol2 and l1[2][0] == p:
                l1[2][0] = symbol
                return l1
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if l1[row][column] == p:
            l1[row][column] = symbol
            return l1
        else:
            continue


comp_easy = False
comp_hard = False
while True:
    game = input("Do you want to play (yes/no): ")
    if game.lower() == "yes":
        vs_comp = input("Do you want to play with compiuter (yes/no):")
        if vs_comp.lower() == "yes":
            while True:
                or_hard = input(
                    "Easy or Hard(e/h):")
                if or_hard.lower() == "e" or or_hard.lower() == "easy":
                    comp_easy = True
                    break
                elif or_hard.lower() == "h" or or_hard.lower() == "hard":
                    comp_hard = True
                    break
                else:
                    print("I do not understand.")
        print("Let's play.")
        break
    elif game.lower() == "no":
        print("Sprry.")
        exit()
    else:
        print("I do not understand.")

p = " "
x = "X"
o = "O"
comp = "Compijuter"

if vs_comp.lower() != "yes":
    player1 = input("Enter the name of the first player: ")
    player2 = input("Enter the name of the second player: ")
    firstPlayer = random.choice([player1, player2])
    if firstPlayer == player1:
        secondPlayer = player2
    else:
        secondPlayer = player1
    while True:
        simbol = input(f"{firstPlayer}, choose whether you want x or o: ")
        if simbol.lower() == "x":
            X = [firstPlayer, x, 0]
            O = [secondPlayer, o, 0]
            start = 0
            break
        elif simbol.lower() == "o" or simbol == "0":
            O = [firstPlayer, o, 0]
            X = [secondPlayer, x, 0]
            start = 1
            break
    print("You not enter X or O. ")
else:
    player1 = input("Enter the name of the player: ")
    while True:
        simbol = input(f"{player1}, choose whether you want x or o: ")
        if simbol.lower() == "x":
            X = [player1, x, 0]
            O = [comp, o, 0]
            start = 0
            break
        elif simbol.lower() == "o" or simbol == "0":
            O = [player1, o, 0]
            X = [comp, x, 0]
            start = 1
            break
p = " "
x = "X"
o = "O"


winer = ""
draw = 0
lastCarX = X[0][-1] == "a"
lastCarO = O[0][-1] == "a"
while True:
    if winer == o or winer == x or draw > 0:
        if winer == o:
            O[2] += 1
        elif winer == x:
            X[2] += 1
        print(f"{X[0]} has won {X[2]} times ")
        print(f"{O[0]} has won {O[2]} times ")
        print(f"Draw: {draw}")
        start += 1
        while True:
            newgame = input("Do you wanth a new game (yes/no): ")
            if newgame.lower() == "yes":
                break
            elif newgame.lower() == "no":
                print("Thank you.")
                exit()
            print("I do not understand.")

    l1 = [[p, p, p], [p, p, p], [p, p, p]]
    table(l1)

    for i in range(start, start + 10):
        if i == start + 9:
            print("Table is full. Draw!")
            draw += 1
            break
        if i % 2 == 0:
            if X[0] == comp:
                compPlay(l1, x, o)
            else:
                l1 = input_row(X)
            winer = end(l1)
            table(l1)
            if winer == x:
                break
        else:
            if O[0] == comp:
                compPlay(l1, o, x)
            else:
                l1 = input_row(O)
            winer = end(l1)
            table(l1)
            if winer == o:
                break
