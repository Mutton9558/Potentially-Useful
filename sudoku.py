import numpy as np

ROW_COUNT = 3
COL_COUNT = 3
game_run = True

def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def print_board(board):
    print(board)

def is_valid_location(board, col, row):
    return board[row][col] == 0

def update_board(board, row, col, piece):
    board[row][col] = piece

board = create_board()
print_board(board)

while game_run:
    row = int(input("Enter a row: "))
    col = int(input("Enter a column: "))
    piece = int(input("Enter a number from 1 to 9: "))
    if piece > 9 or piece < 1:
        print("Invalid location!")
        continue
    for i in range(3):
        for j in range(3):
            if board[i][j] == piece:
                print("Number invalid!")
                break
            else:
                continue
    if is_valid_location(board, col, row):
        update_board(board, row, col, piece)
    else:
        print("Invalid location!")
    print_board(board)
