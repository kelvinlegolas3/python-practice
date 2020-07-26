def initialize_player_inputs():
    is_symbol_valid = False

    while not is_symbol_valid:
        player1_symbol = input("Choose 1st player's symbol: ")
        player2_symbol = input("Choose 2nd player's symbol: ")
        
        if player1_symbol != player2_symbol and not player1_symbol.isspace() and not player2_symbol.isspace():
            is_symbol_valid = True
            
        else:
            print("Error: Invalid inputs for Player 1 or Player 2. Try again")
            
    else:
        return player1_symbol, player2_symbol


def initialize_table():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


def visualize_table(table):
    print(f"{table[0]}\n{table[1]}\n{table[2]}")


def change_table(table):
    is_input_valid = False

    while not is_input_valid:
        try:
            first_move, second_move = input(f"What's your move? [{current_player}]: ").split()
            first_move = int(first_move)
            second_move = int(second_move)
            
            if(first_move < 0 or second_move < 0):
                print("Error: Invalid integer value")
                
            elif not table[first_move][second_move].isspace():
                print("Error: Position has already been taken")
                
            else:
                is_input_valid = True
                
        except IndexError:
            print("Error: Invalid index")
            
        except ValueError:
            print("Error: Invalid input")

    else:
        table[int(first_move)][int(second_move)] = current_player

    return table


def switch_players(player):
    if player == players["Player 1"]:
        player = players["Player 2"]
        
    else:
        player = players["Player 1"]
        
    return player


def validate_combination(combination):
    if not combination.isspace() and combination[0]*3 == combination:
        return True


def is_game_over(table):
    combinations = []
    slash_combination = ""
    backslash_combination = ""
    
    for index, row in enumerate(table):
        row_combination = "".join(row)
        combinations.append(row_combination)
        
        columns = [x[index] for x in table]
        column_combination = "".join(columns)
        combinations.append(column_combination)
        
        slash_combination = slash_combination + row[index]
        combinations.append(slash_combination)
        
        backslash_combination = backslash_combination + row[::-1][index]
        combinations.append(backslash_combination)

    print(f"Debug: {combinations}")
    possibilities = list(filter(validate_combination, combinations))
    
    return len(possibilities) > 0


# Tic Tac Toe - Game
tictactoe_table = initialize_table()
player1, player2 = initialize_player_inputs()

players = {"Player 1": player1, "Player 2": player2}
current_player = players["Player 1"]

while not is_game_over(tictactoe_table):
    tictactoe_table = change_table(tictactoe_table)
    current_player = switch_players(current_player)
    
    visualize_table(tictactoe_table)
    
else:
    print("Game over! Congratulations!")