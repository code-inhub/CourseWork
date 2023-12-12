import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):

    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return -1
    if is_winner(board, 'O'):
        return 1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float('inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe")
    print_board(board)
    while True:
        row, col = get_best_move(board)
        board[row][col] = 'O'
        print("\nComputer's move:")
        print_board(board)

        if is_winner(board, 'O'):
            print("\nComputer wins!")
            break
        elif is_draw(board):
            print("\nIt's a draw!")
            break

        player_row = int(input("\nEnter your move (row 1-3): ")) - 1
        player_col = int(input("Enter your move (column 1-3): ")) - 1

        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'X'
        else:
            print("Invalid move! Try again.")
            continue

        print("\nYour move:")
        print_board(board)

        if is_winner(board, 'X'):
            print("\nYou win!")
            break
        elif is_draw(board):
            print("\nIt's a draw!")
            break

if __name__ == '__main__':
    main()