def initialize_table():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


def change_table(first_move, second_move, table, symbol):
    table[int(first_move)][int(second_move)] = symbol
    return table


def visualize_table(table):
    return f"{table[0]}\n{table[1]}\n{table[2]}"


def is_game_over(table):
    result = False

    #Horizontal
    for row in table:
        filled_row = "".join(row)
        if filled_row == "XXX" or filled_row == "OOO":
            result = True

    #Vertical
    for index, row in enumerate(table):
        column = [x[index] for x in table]
        filled_column = "".join(column)
        if filled_column == "XXX" or filled_column == "OOO":
            result = True

    #Slash
    slash_combination = ""
    for index, row in enumerate(table):
        slash_combination = slash_combination + row[index]
    if slash_combination == "XXX" or slash_combination == "OOO":
        result = True

    #Backslash
    backslash_combination = ""
    for index, row in enumerate(table):
        backslash_combination = backslash_combination + row[::-1][index]
    if backslash_combination == "XXX" or backslash_combination == "OOO":
        result = True

    return result


player1_symbol = input("Choose 1st player's symbol: ")
player2_symbol = input("Choose 2nd player's symbol: ")
game_table = initialize_table()
symbol = player1_symbol

while not is_game_over(game_table):
    player_first_move, player_second_move = input("What's your move?: ").split()
    round_table_result = change_table(player_first_move, player_second_move, game_table, symbol)

    if symbol == player1_symbol:
        symbol = player2_symbol
    else:
        symbol = player1_symbol

    print(visualize_table(round_table_result))