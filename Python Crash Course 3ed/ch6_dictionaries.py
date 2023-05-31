""" Python Crash Course - Chapter 6 - Dictionaries """

# Python Dictionaries are collections of key-value pairs.
# Nesting is the process of storing multiple dictionaries
# in a list, a list of items in a dictionary,
# or even a dictionary inside another dictionary.

# A Knight is a character in a game with the following attributes:
knight = {
    'hp': '100',
    'mana': '50',
    'helmet': 'royal helmet',
    'helmet2': 'royal helmet',
    }

# A Wizard is a character in a game with the following attributes:
wizard = {
    'hp': '50',
    'mana': '150',
    'weapon': 'death wand',
    'shield': 'spellbook',
    'helmet': "Rabadon's deathcap",
    }

# A Paladin is a character in a game with the following attributes:
paladin = {
    'hp': '75',
    'mana': '75',
    'weapon': 'arbalest',
    'shield': 'light shield',
    'helmet': 'skull helmet',
    }

# Retrieve value from dictionary:
print("\nRetrieve value from dictionary:")
print(f"Knight's HP: {knight['hp']}")

# Adding new attributes to a dictionary:
print("\nAdding new attributes to a dictionary:")
knight['shield'] = 'blessed shield'
knight['weapon'] = 'fire axe'
print(f"Knight's armor: {knight['weapon']}")
print(f"Knight's shield: {knight['shield']}")

# Change value of an attribute in dictionary:
print("\nChange value of an attribute in dictionary:")
knight['shield'] = 'dragon scale shield'
knight['weapon'] = 'ice hammer'
print(f"Knight's new shield: {knight['shield']}")
print(f"Knight's new weapon: {knight['weapon']}")

# Deleting an attribute from a dictionary:
print("\nDeleting an attribute from a dictionary:")
del knight['helmet2']
# returns "no helmet" if key "helmet" does not exist
print(f"Knight's helmet: {knight.get('helmet', 'no helmet')}")

# Looping through all key-value pairs:
print("\nLooping through all key-value pairs:")
for attribute, value in knight.items():
    print(f"Attribute: {attribute} Value: {value}")

# Looping through all keys:
print("\nLooping through all keys:")
for attribute in knight:
    print(f"Attribute: {attribute}")

# Looping through all values:
print("\nLooping through all values:")
for value in knight.values():
    print(f"Value: {value}")

# Looping through sorted dictionary keys:
print("\nLooping through sorted dictionary keys:")
for key in sorted(knight.keys()):
    print(f"Attribute: {key} Value: {knight[key]}")

# Looping through non repetitive iterator(values):
print("\nLooping through non repetitive iterator(values):")
for values in sorted(set(knight.values())):
    print(f"Value: {values}")

# Creating a list of dictionaries and duplicate each character hp and mana:
print("\nCreating a list of dictionaries and x2 each character hp and mana:")
team = [knight, wizard, paladin]
# Adding more hp and mana to each character:
for character in team:
    character['hp'] = str(int(character['hp']) * 2)
    character['mana'] = str(int(character['mana']) * 2)
    print(character)

# Dictionaries inside dictionaries:
print("\nDictionaries inside dictionaries:")
knight = {
    'hp': '100',
    'mana': '50',
    'helmet': 'royal helmet',
    'weapon': {
        'name': 'serpent sword',
        'atk': '50',
        'def': '30',
        'weight': '50.00 oz',
        },
    'shield': {
        'name': 'thorn shield',
        'atk': '0',
        'def': '60',
        'weight': '60.00 oz',
        },
    }

# Looping through nested dictionaries:
print("\nLooping through nested dictionaries:")
for attribute, value in knight.items():
    if isinstance(value, dict):
        print(f"\n{attribute.title()}:")
        for stat in value:
            print(f"\t{stat.title()}: {value[stat]}")
    else:
        print(f"\n{attribute.title()}: \n\t{value}")
