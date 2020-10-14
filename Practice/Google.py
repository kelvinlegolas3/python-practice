


# Exercise # 2:
def solution2(l, t):
    number_list = l
    total = t
    
    for index, number in enumerate(number_list):
        for index2, number2 in enumerate(number_list):
            if sum(number_list[index:index2+1]) == total:
                return [index, index2]
    return [-1, -1]
    
    
print(solution2([1, 11, 10, 2, 8], 12))

# Exercise # 3:
def solution3(pegs):
    pegs_set = set(pegs)