# Assessment 3  : Python Statements
# Link          : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

# 1.
print("Exercise # 1:")


def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return num1 if num1 < num2 else num2
    elif num1 % 2 != 0 or num2 % 2 != 0:
        return num1 if num1 > num2 else num2


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))

# 2.
print("\nExercise # 2:")


def animal_crackers(animals):
    animal_first_letter = [x[0] for x in animals.split(" ")]
    return True if animal_first_letter[0] == animal_first_letter[1] else False


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))

# 3.
print("\nExercise # 3:")


def makes_twenty(num1, num2):
    return True if num1 + num2 == 20 or num1 == 20 or num2 == 20 else False


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))

# 4.
print("\nExercise # 4:")


def old_macdonald(name):
    name_to_letters_list = [x[0] for x in name]
    result = ""
    for index, letter in enumerate(name_to_letters_list):
        if index == 0 or index == 3:
            letter = letter.capitalize()
        result = result + letter
    return result


print(old_macdonald("macdonald"))

# 5.
print("\nExercise # 5:")


def master_yoda(words):
    word_list = [x for x in words.split(" ")]
    reversed_list = word_list[::-1]
    return " ".join(reversed_list)


print(master_yoda("I am home"))
print(master_yoda("We are ready"))

# 6.
print("\nExercise # 6:")


def almost_there(num):
    return abs(100 - num) <= 10 or abs(200 - num) <= 10


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# 7.
print("\nExercise # 7:")


def has_33(nums):
    result = ""
    for num in nums:
        result = result + str(num)
    return True if "33" in result else False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# 8.
print("\nExercise # 8:")


def paper_doll(word):
    tripled_letters = [x*3 for x in word]
    return "".join(tripled_letters)


print(paper_doll("Hello"))
print(paper_doll('Mississippi'))

# 9.
print("\nExercise # 9:")


def black_jack(num1, num2, num3):
    cards = [num1, num2, num3]
    summation = sum(cards)
    if summation > 21 and 11 in cards:
        summation = summation - 10
    return str(summation) if summation <= 21 else "BUST"


print(black_jack(5, 6, 7))
print(black_jack(9, 9, 9))
print(black_jack(9, 9, 11))


# 10.
print("\nExercise # 10:")


def summer_69(nums):
    total = 0
    for index, num in enumerate(nums):
        if 6 in nums and 9 in nums:
            six_index = nums.index(6)
            nine_index = nums.index(9)
            if index < six_index or index > nine_index:
                total = total + num
        else:
            total = total + num

    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# 11.
print("\nExercise # 11:")


def spy_game(nums):
    result = ""
    for num in nums:
        result = result + str(num)
    return True if "007" in result else False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))