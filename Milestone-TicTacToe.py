def initialize_table():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


def visualize_table(table):
    return f"{table[0]}\n{table[1]}\n{table[2]}"


def change_table(table, symbol):
    is_input_valid = False

    while not is_input_valid:
        first_move, second_move = input("What's your move?: ").split()
        try:
            if table[int(first_move)][int(second_move)] == " ":
                is_input_valid = True
            else:
                print("Error: Position has already been taken")
        except IndexError:
            print("Error: Invalid index")

    else:
        is_input_valid = True
        table[int(first_move)][int(second_move)] = symbol

    return table


def is_game_over(table):
    result = False

    for row in table:
        row_combination = "".join(row)
        if row_combination == "XXX" or row_combination == "OOO":
            return True

    for index, row in enumerate(table):
        columns = [x[index] for x in table]
        column_combination = "".join(columns)
        if column_combination == "XXX" or column_combination == "OOO":
            return True

    slash_combination = ""
    for index, row in enumerate(table):
        slash_combination = slash_combination + row[index]
        if slash_combination == "XXX" or slash_combination == "OOO":
            return True

    backslash_combination = ""
    for index, row in enumerate(table):
        backslash_combination = backslash_combination + row[::-1][index]
        if backslash_combination == "XXX" or backslash_combination == "OOO":
            return True

    return result


# Tic Tac Toe - Game
player1_symbol = input("Choose 1st player's symbol: ")
player2_symbol = input("Choose 2nd player's symbol: ")

tictactoe_table = initialize_table()
symbol = player1_symbol

while not is_game_over(tictactoe_table):
    round_table_result = change_table(tictactoe_table, symbol)

    if symbol == player1_symbol:
        symbol = player2_symbol
    else:
        symbol = player1_symbol

    print(visualize_table(round_table_result))
else:
    print("Game over! Congratulations!")