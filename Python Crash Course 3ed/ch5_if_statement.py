""" Python Crash Course - Chapter 5 - If Statements """
# Python If Statements are used to examine the current state of a program
# and respond appropriately to that state.
# If statements examples:
# Numerical comparisons:
print("Numerical comparisons:")
num1 = -5
if num1 >= 0:
    print("The number is positive")
else:
    print("The number is negative")

print("\nString comparisons:")
# String comparisons:
string1 = ""
if string1:
    print("The string is not empty")
else:
    print("The string is empty")

# Checking if a value is in a list:
print("\nChecking if a value is in a list:")
fruits = ['apple', 'banana', 'orange']
if 'banana' in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")

# Checking if a value is not in a list:
print("\nChecking if a value is not in a list:")
fruits = ['apple', 'banana', 'orange']
if 'pineapple' not in fruits:
    print("Pineapple is not in the list")
else:
    print("Pineapple is in the list")

# Multiple conditions:
print("\nChecking multiple conditions:")
fruits = ['apple', 'banana', 'orange']
if 'banana' in fruits and len(fruits) > 2:
    print("The list contains banana and has more than 2 elements")
else:
    print("The list does not meet both conditions")

# Checking 2 names are different
print("\nChecking 2 names are different:")   
name1 = 'John'
name2 = 'Juan'
if name1 != name2:
    print("The names are different")

# Else if statements:
print("\nChecking Else if statements:")
fruits = ['apple', 'banana', 'orange']
if 'pineapple' in fruits:
    # code to execute if condition is True
    print("The list contains pineapple")
elif 'watermelon' in fruits:
    print("The list contains watermelon")
else:
    # code to execute if condition is False
    print("The list does not contain pineapple or watermelon")

fruits = ('apple', 'banana', 'orange', 'watermelon', 'pineapple', 'grape')
requested_fruits = ['apple', 'Blueberry', 'banana', 'strawberry', 'watermelon',
                    'raspberry', 'grape', 'kiwi']

# Checking if list values are in other list:
print("\nChecking if list values are in other list:")
for req_fruit in requested_fruits:
    if req_fruit in fruits:
        print(f"Adding {req_fruit} to the basket")
    else:
        print(f"{req_fruit} is not available")
