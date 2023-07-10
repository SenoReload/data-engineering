""" Python Crash Course - Chapter 7 - User Input and While Loops """
# A While Loop is used to run a block of code as long as a certain
# condition is true.
# An Python User Input is a way to get information from the user.
num_people = int(input("How many people are in your dinner group? "))

if num_people > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready. Please follow me.")

# The Modulo Operator (%) divides one number by another number and returns the
# remainder.If the number is divisible by the other number, the remainder is 0.
number = int(input("Is this number a multiple of 10?: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

# A While Loop runs as long as a certain condition is true.
# A Flag is a variable that determines when a program should stop running.
FLAG = True
while FLAG:
    number = int(input("Is this number a multiple of 10?: "))
    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
        FLAG = False
    else:
        print(f"{number} is not a multiple of 10.")

# Break statements can be used to exit a loop.
# Continue statements can be used to skip over certain parts of a loop.
list_random_words = ["cat", "dog", "bird", "fish", "horse", "snake", "mouse"]
X = 0
FLAG = True
while FLAG:  # active flag. Ends after entering 3 words in list.
    word = input("Enter a word: ")
    if word == "quit":
        print("Goodbye!")
        break  # break statement. Ends if "quit" is entered.
    if word not in list_random_words:
        print(f"{word} is not in the list.")
        continue  # continue statement. Avoid printing "is in the list".
    print(f"{word} is in the list.")
    if X >= 3:  # active variable. Flag turns false after 3 words entered.
        FLAG = False
    else:
        X += 1
