# Assessment 2  : Python Statements
# Link          : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/07-Statements%20Assessment%20Test.ipynb

# 1.
print("Exercise # 1:")
string1 = "Print only the words that start with s in this sentence"
splittedString1 = string1.split(" ")
s_list = [s for s in splittedString1 if s[0].lower().count('s') != 0]

print(f"Given: {string1}")
print(f"List of words that starts with an 's' on it: {s_list}")

# 2.
print("\nExercise # 2:")
even_list = [even for even in list(range(11)) if even % 2 == 0]
print(f"List of even numbers from 1 to 11: {even_list}")

# 3.
print("\nExercise # 3:")
list3 = [x for x in range(1, 51) if x % 3 == 0]
print(list3)

# 4.
print("\nExercise # 4:")
string4 = 'Print every word in this sentence that has an even number of letters'
splittedString4 = string4.split(" ")
for word in splittedString4:
    wordLength = len(word)
    numType = "odd"
    if wordLength % 2 == 0:
        num_type = "even"
    print(f"'{word}' has a length of {wordLength} which is an {numType} number.")

# 5.
print("\nExercise # 5:")
integers5 = list(range(1, 101))
for integer in integers5:
    if integer % 3 == 0 and integer % 5 == 0:
        print("FizzBuzz")
    elif integer % 3 == 0:
        print("Fizz")
    elif integer % 5 == 0:
        print("Buzz")
    else:
        print(integer)

# 6.
print("\nExercise # 6:")
string6 = 'Create a list of the first letters of every word in this string'
list6 = [x[0] for x in string6.split(" ")]
print(list6)
