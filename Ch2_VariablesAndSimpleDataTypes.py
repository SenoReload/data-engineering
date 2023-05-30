# f-strings: formating varible values to strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"No Strips:\n\tHello,   {full_name.title()}  !   ")
print(f"Strips:\n\tHello,   {full_name.title()}  !   ".strip().removeprefix("Strips:").removesuffix("!"))

# Numbers
# Arbitrary number of decimal places
print(0.2 + 0.1)
print(3 * 0.1)

# Multiple assignments
x, y, z = 0, 0, 0

# Constants and underscores
MAX_CONNECTIONS = 5_0_0_0
print(MAX_CONNECTIONS)