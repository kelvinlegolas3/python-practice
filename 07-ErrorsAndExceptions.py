# Assessment 7  : Errors and Exceptions
# Link          : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/07-Errors%20and%20Exception%20Handling/02-Errors%20and%20Exceptions%20Homework.ipynb

# 1.
print("Exercise # 1:")
for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print("You're not allowed to raise a string to a number")


# 2.
print("Exercise # 2:")
x = 5
y = 0

try:
    z = x/y
except:
    print("You can't divide a number by zero")
finally:
    print("All done")    
    

# 3.
print("Exercise # 3:")
def square_of_a_number():
    while True:
        try:
            number = int(input("Input a number: "))
            number = number ** 2
        except:
            print("Please provide a number instead of anything else")
            continue
        else:
            print(f"The square of your number is: {number}")
            break

square_of_a_number()