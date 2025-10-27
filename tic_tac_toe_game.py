from collections import deque

board_numeration = []
positions = {}
number = 1
for i in range(3):
    row = []
    for j in range(3):
        row.append(f"  {number}  ")
        positions[number] = (i, j)
        number += 1
    board_numeration.append(row)

player_one = input("Player one name: ")
player_two = input("Player two name: ")

while player_one == player_two:
    print("This name is the same as player one.")
    player_two = input("PLease provide a name for player two different than player one: ")

player_one_sign = input(f"{player_one}, would you like to play with 'X' or 'O'? ")
while player_one_sign not in ["X", "x", "O", "o"]:
    player_one_sign = input(f"{player_one}, please enter a valid symbol - 'X' or 'O': ")

if player_one_sign in "Xx":
    player_one_sign = "X"
    player_two_sign = "O"
else:
    player_one_sign = "O"
    player_two_sign = "X"


player_symbol = {player_one: player_one_sign, player_two: player_two_sign}

print("This is the numeration of the board:")
for row in board_numeration:
    print("|", end="")
    print(*row, sep="|", end="")
    print("|")

print(f"{player_one} starts first!")

players = deque([player_one, player_two])

while True:
    board = [[" " for _ in range(3)] for _ in range(3)]

    player_won = False
    filled_cells = []

    while True:
        player_in_turn = players[0]

        while True:
            try:
                position = int(input(f"{player_in_turn}, choose a free position [1-9]: "))
            except ValueError:
                print(f"Not a valid position!")
            else:
                if not(1 <= position <= 9 and position not in filled_cells):
                    print("Position should be a number between 1 and 9, which is free")
                else:
                    break
        row, col = positions[position]
        board[row][col] = player_symbol[player_in_turn]
        filled_cells.append(position)

        for row in board:
            print("|  ", end="")
            print("  |  ".join(row), end="")
            print("  |")

        if len(filled_cells) >= 5:
            for row in board:
                if row[0] != " " and row[1] != " " and row[2] != " " and row[0] == row[1] == row[2]:
                    player_won = True
                    break
            else:
                for i in range(3):
                    if board[0][i] != " " and board[1][i] != " " and board[2][i] != " " and board[0][i] == board[1][i] == board[2][i]:
                        player_won = True
                        break
                else:
                    if (board[0][0] != " " and board[1][1] != " " and board[2][2] != " " and board[0][0] == board[1][1] == board[2][2]) or \
                            (board[0][2] != " " and board[1][1] != " " and board[2][0] != " " and board[0][2] == board[1][1] == board[2][0]):
                        player_won = True
            if player_won:
                print(f"{player_in_turn} won!")
                break
        if len(filled_cells) == 9:
            print("Board full, no one wins.")
            break

        players.rotate()

    play_again = input("Wanna play again? Y or N: ").upper()
    while play_again not in "YN":
        print("Invalid input.")
        play_again = input("Wanna play again? Y or N: ").upper()

    if play_again == "N":
        break

print("Thank you for playing!")