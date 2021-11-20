
# program solves a sudoku puzzle by itself; using backtracking algorithm

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if (bo[i][j]) == 0:
                return (i, j)  # row, col

    return None


def valid(bo, num, pos):

    # Check row

    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    return True


def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])


def solve(bo):

    find = find_empty(bo)
    if not find:
        return True

    else:
        row, col = find

    for i in range(1, 4):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


board = [
    [1, 0, 2, ],
    [0, 2, 0, ],
    [2, 0, 3, ]
]


print("PUZZLE:")
print_board(board)
solve(board)
print()
print("SOLUTION:")
print_board(board)


#print (len(board[0]))
