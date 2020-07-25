def validate_combination(combination):
    if not row_combination.isspace() and combination[0]*3 == combination:
        return True
    else:
        return False
    return True


table = [["X", "X", "X"],
 [" ", " ", " "],
 [" ", " ", " "]]

result = False

for row in table:
    row_combination = "".join(row)
    result = validate_combination(row_combination)

print(result)