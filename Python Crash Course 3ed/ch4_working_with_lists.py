""" Python Crash Course - Chapter 4 - Working with Lists """
# A Python List is a collection of items in a particular order.
# A Python slice is a specific group of items in a list.
# Python Tuples are immutable lists.

# A list of 5 names
names = ["jose", "maria", "juan", "pedro", "luis"]

# Greet each person in the list
for name in names:
    print("Hola,", name.title(), "!")

# A list of numbers
num_list = [x**x for x in range(2, 7)]
print(num_list)

# Get the minimum and maximum values
print("The minimum value is", min(num_list))
print("The maximum value is", max(num_list))

# A slice of the list
print("\nSlice of the list:", num_list[2:6])

# A slice of the 3 first items
print("\nSlice of the 3 first items:", num_list[:3])

# A slice of the 3 last items
print("\nSlice of the 3 last items:", num_list[-3:])  # Negative index

# A slice of the list 2-by-2
print("\nSlice of the list:", num_list[2:6:2], "\n")  # 2-by-2

# Looping through a slice
for number in num_list[2:6]:
    print("Looping through Slice:", number)

# Copying a list
new_number_list = num_list[:]

# Proving that the lists are different
num_list.append(100)  # Adding a new element to the original list
print("\nNew Number List:", new_number_list)

# Defining a Tuple
my_tuple = (1, 2, 3, 4, 5)

# Iterating through a tuple slice
print("\nIterating through a tuple slice:")
for num in my_tuple[1:4]:
    print("Tuple Element:", num)
