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


def validate_combination(combination):
    if not combination.isspace() and combination[0]*3 == combination:
        return True


def is_game_over(table):
    for row in table:
        row_combination = "".join(row)
        return validate_combination(row_combination)

    for index, row in enumerate(table):
        columns = [x[index] for x in table]
        column_combination = "".join(columns)
        return validate_combination(column_combination)

    slash_combination = ""
    for index, row in enumerate(table):
        slash_combination = slash_combination + row[index]
        return validate_combination(slash_combination)

    backslash_combination = ""
    for index, row in enumerate(table):
        backslash_combination = backslash_combination + row[::-1][index]
        return validate_combination(backslash_combination)


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

else:
    print("We got a winner!")