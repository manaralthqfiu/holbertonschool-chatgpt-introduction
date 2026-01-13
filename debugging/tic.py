#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input validation
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Range validation
        if row not in [0,1,2] or col not in [0,1,2]:
            print("Invalid position. Choose 0, 1, or 2.")
            continue

        # Spot taken
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place move
        board[row][col] = player

        # Check win
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Check tie
        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
