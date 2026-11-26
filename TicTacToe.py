# Tic Tac Toe Game

board = [" " for i in range(9)]


def display():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i : i + 3]))
        if i < 6:
            print("--+---+--")


def check_winner(player):
    win_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for pos in win_positions:
        if (
            board[pos[0]] == player
            and board[pos[1]] == player
            and board[pos[2]] == player
        ):
            return True

    return False


def tic_tac_toe():
    player = "X"

    for turn in range(9):
        display()
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid move! Try again.")
            continue

        board[position] = player

        if check_winner(player):
            display()
            print(player, "wins!")
            return

        player = "O" if player == "X" else "X"

    display()
    print("Game is a Draw!")


tic_tac_toe()
