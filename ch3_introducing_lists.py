# A Python List is a collection of items in a particular order.
months = ["jan", "february", "march", "april", "may", "july", "august", "september", "october", "november"]

# Accessing Elements
# Indexing starts at 0
print("First item is ", months[0].title(), "with Index: 0") # "january"

# Last month: wheter the list is sorted or not, last item index is -1 or len(list) - 1
print("Last item is ", months[-1].title(), "with Index: -1") # "december" or
print("Last item is ", months[len(months) - 1].title(), "with Index: len(months) - 1") # "december"

# List of places
places = ["first", "second", "third", "fourth", "fifth", "seventh", "eighth", "nineth", "tenth", "eleventh"]
    
# Modifying Elements
# Change the first month to "january"
months[0] = "january"

# Add a month to the end of the list
months.append("december")
places.append("twelveth")

# Add a month in any position of the list
months.insert(5, "june")
places.insert(5, "sixth")

# Zip function: combines two lists into a list of tuples
# Print the months and places
print("\nPlaces and Months:")
for month, place in zip(months, places):
    print(f"The {place.title()} month of the year is {month.title()}")

# Deleting Elements
# Remove the last month from the list
print("\nDeleting Elements:")
last_month = months.pop() # Remove the last month from the list
last_place = places.pop() # Remove the last place from the list
print(f"The last month of the year is {last_month.title()} which is {last_place.title()}")

# Remove an item by value
print("\nRemoving Elements by Values: january and first")
months.remove("january") # Remove the first month from the list
places.remove("first") # Remove the first place from the list
print(months, places)

# Sorting List Temporarily
print("\nSorting Elements Temporarily:")
# Python Crash Course - Chapter 3 - Working with Lists
# Sorting a List in reverse order
print(sorted(months), "\n", sorted(places, reverse=True))

# Sorting a List Permanently: sorting months alphabetically
months.sort()

# Sorting a List in reverse order
places.sort(reverse=True)

print("\nSorting Elements Permanently:")
print(months,"\n",  places)

# Reversing Lists
print("\nReversing Lists:")
months.reverse()
places.reverse()
print(months, "\n", places) # Returns a reversed iterator

# Length of a List
print("Lenght of months: ", len(months), "\nLenght of places: ", len(places))
