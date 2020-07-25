# Assessment 3  : Functions v2
# Link          : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/08-Functions%20and%20Methods%20Homework.ipynb

# 1.
print("Exercise # 1:")


from math import pi
def sphere_volume(radius):
    return 4/3 * pi * radius ** 3

print(sphere_volume(2))

# 2.
print("\nExercise # 2:")


def is_number_in_between(num, low, high):
    return True if num > low and num < high else False


print(is_number_in_between(3, 1, 5))

# 3.
print("\nExercise # 3:")


def up_low(statement):
    uppercase_list = [x for x in statement if x.isupper()]
    lowercase_list = [x for x in statement if x.islower()]

    print(f"The statement is: {statement}")
    print(f"# of uppercase: {len(uppercase_list)}")
    print(f"# of lowercase: {len(lowercase_list)}")


print(up_low("Hello hOw are you today?"))
print(up_low("AwTs DuTeRtE"))

# 4.
print("\nExercise # 4:")


def unique(nums):
    return [x for x in set(nums)]


print(unique([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

# 5.
print("\nExercise # 5:")


def multiply(nums):
    result = 1
    for num in nums:
        result = result * num
    return result


print(multiply([1, 2, 3, 4]))


# 6.
print("\nExercise # 6:")


def palindrome(word):
    return True if word.lower() == word[::-1].lower() else False


print(palindrome("Toyota"))
print(palindrome("Helleh"))


# 7.
print("\nExercise # 7:")


import string
def ispangram(statement):
    alphabet_list = set(string.ascii_lowercase)
    statement = statement.replace(" ", "").lower()
    statement = set(statement)

    return statement == alphabet_list


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("abcdefghijklmnopqrstuvwxyz"))