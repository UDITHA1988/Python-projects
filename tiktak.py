# function to check if three "X" or "O" marks are in line.
def chk(bo):

    if (
        bo[0][0] == bo[0][1] == bo[0][2]
        or bo[1][0] == bo[1][1] == bo[1][2]
        or bo[2][0] == bo[2][1] == bo[2][2]
        or bo[0][0] == bo[1][1] == bo[2][2]
        or bo[2][0] == bo[1][1] == bo[0][2]
    ):
        return "win"


# function to get input from player 1 and mark them on the board.
def inputX(pl, bo):

    if pl == 1:
        bo[0][0] = "X"

    elif pl == 2:
        bo[0][1] = "X"

    elif pl == 3:
        bo[0][2] = "X"

    elif pl == 4:
        bo[1][0] = "X"

    elif pl == 5:
        bo[1][1] = "X"

    elif pl == 6:
        bo[1][2] = "X"

    elif pl == 7:
        bo[2][0] = "X"

    elif pl == 8:
        bo[2][1] = "X"

    elif pl == 9:
        bo[2][2] = "X"


# function to get input from player 2 and mark them on the board.
def inputO(pl, bo):

    if pl == 1:
        bo[0][0] = "O"

    elif pl == 2:
        bo[0][1] = "O"

    elif pl == 3:
        bo[0][2] = "O"

    elif pl == 4:
        bo[1][0] = "O"

    elif pl == 5:
        bo[1][1] = "O"

    elif pl == 6:
        bo[1][2] = "O"

    elif pl == 7:
        bo[2][0] = "O"

    elif pl == 8:
        bo[2][1] = "O"

    elif pl == 9:
        bo[2][2] = "O"


# function to print the board.
def printBoard(bo):

    print()
    print(bo[0])
    print(bo[1])
    print(bo[2])
    print()


# main function.
def play(bo):

    printBoard(bo)
    pl1 = int(input("INPUT PLAYER 1:"))
    inputX(pl1, bo)
    printBoard(bo)

    if chk(bo) == "win":

        print("PLAYER 1 HAS WON")

    else:
        pl2 = int(input("INPUT PLAYER 2:"))
        inputO(pl2, bo)
        printBoard(bo)

        if chk(bo) == "win":
            print("PLAYER 2 HAS WON")

        else:
            play(bo)


bo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

play(bo)
