# Solves a 'Sudoku' grid by using Backtracking Algorithm
# # pick empty ## try all options ## find one that works Repeat ## backtrack if error encountered

grid = [ 
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]


# backtracking solution 

def solve_board(board):

    find = find_empty_spaces(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if check_validity(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True
            
            board[row][col] = 0
    
    return False


# checks if inserted number is valid for the position

def check_validity(board, num, posi):

    # row checking
    for i in range(len(board[0])):
        # check if any element in all cols. of row are equal to ip but not in the position of recent insertion
        if board[posi[0]][i] == num and posi[1] != i:
            return False

    # column checking
    for i in range(len(board)):
        # check if any element in all rows. of col are equal to ip but not in the position of recent insertion
        if board[i][posi[1]] == num and posi[0] != i:
            return False

    # box checking
    xbox = posi[1] // 3           # integer division, takes us to a certain box
    ybox = posi[0] // 3

# helps us reach an element in the board
    for i in range(ybox*3, ybox*3+3):
        for j in range(xbox*3, xbox*3+3):
            # check if any element in all rows, cols of the box are = to ip but not in the position of recent insertion
            if board[i][j] == num and (i,j) != posi:
                return False

    return True


def print_the_board(board):

    # row divisions

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        
    # column division

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

        # print board elements

            if j == 8:
                # last line
                print(board[i][j])
            else:
                # intermediate lines
                print(str(board[i][j]) + " ", end="")


# print_the_board(grid)

# # i is row j is col

def find_empty_spaces(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


print("This is the Input Grid \n")
print(" ")
print_the_board(grid)
solve_board(grid)
print("\n This is the Solved Board")
print(" ")
print_the_board(grid)