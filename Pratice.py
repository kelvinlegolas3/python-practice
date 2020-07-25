def initialize_table():
    return [["X", "X", "O"],
            ["O", "O", "O"],
            ["X", "X", "O"]]


def is_game_over(table):
    result = False

    for row in table:
        filled_row = "".join(row)
        if filled_row == "XXX" or filled_row == "OOO":
            result = True

    for index, row in enumerate(table):
        columns = [x[index] for x in table]
        filled_columns = "".join(columns)
        if filled_columns == "XXX" or filled_columns == "OOO":
            result = True

    slash_combination = ""
    for index, row in enumerate(table):
        slash_combination = slash_combination + row[index]
    if slash_combination == "XXX" or slash_combination == "OOO":
        result = True

    backslash_combination = ""
    for index, row in enumerate(table):
        backslash_combination = backslash_combination + row[::-1][index]
    if backslash_combination == "XXX" or backslash_combination == "OOO":
        result = True

    return result


print(is_game_over(initialize_table()))
#is_game_over(initialize_table())
