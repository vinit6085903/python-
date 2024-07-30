# Integer to Float
print("Integer to Float:")
int_val = 10
float_val = float(int_val)
print(f"Integer {int_val} to Float: {float_val}")

# Float to Integer
print("\nFloat to Integer:")
float_val = 10.75
int_val = int(float_val)  # This truncates the decimal part
print(f"Float {float_val} to Integer: {int_val}")

# Integer to String
print("\nInteger to String:")
int_val = 123
str_val = str(int_val)
print(f"Integer {int_val} to String: {str_val}")

# String to Integer
print("\nString to Integer:")
str_val = "456"
int_val = int(str_val)
print(f"String '{str_val}' to Integer: {int_val}")

# Float to String
print("\nFloat to String:")
float_val = 12.34
str_val = str(float_val)
print(f"Float {float_val} to String: {str_val}")

# String to Float
print("\nString to Float:")
str_val = "56.78"
float_val = float(str_val)
print(f"String '{str_val}' to Float: {float_val}")

# List to Tuple
print("\nList to Tuple:")
list_val = [1, 2, 3, 4]
tuple_val = tuple(list_val)
print(f"List {list_val} to Tuple: {tuple_val}")

# Tuple to List
print("\nTuple to List:")
tuple_val = (5, 6, 7, 8)
list_val = list(tuple_val)
print(f"Tuple {tuple_val} to List: {list_val}")

# String to List
print("\nString to List:")
str_val = "hello"
list_val = list(str_val)  # Converts each character to a list element
print(f"String '{str_val}' to List: {list_val}")

# List to String
print("\nList to String:")
list_val = ['h', 'e', 'l', 'l', 'o']
str_val = ''.join(list_val)  # Join list elements into a single string
print(f"List {list_val} to String: '{str_val}'")

# Set to List
print("\nSet to List:")
set_val = {1, 2, 3}
list_val = list(set_val)
print(f"Set {set_val} to List: {list_val}")

# List to Set
print("\nList to Set:")
list_val = [1, 2, 3, 3, 2, 1]
set_val = set(list_val)  # Removes duplicates
print(f"List {list_val} to Set: {set_val}")

# Dictionary to List of Tuples
print("\nDictionary to List of Tuples:")
dict_val = {'a': 1, 'b': 2}
list_val = list(dict_val.items())  # Convert dictionary items to list of tuples
print(f"Dictionary {dict_val} to List of Tuples: {list_val}")

# List of Tuples to Dictionary
print("\nList of Tuples to Dictionary:")
list_val = [('a', 1), ('b', 2)]
dict_val = dict(list_val)  # Convert list of tuples back to dictionary
print(f"List of Tuples {list_val} to Dictionary: {dict_val}")

# Tuple to Dictionary
print("\nTuple to Dictionary (with predefined keys):")
tuple_val = (1, 2, 3)
dict_val = dict(zip(['a', 'b', 'c'], tuple_val))
print(f"Tuple {tuple_val} to Dictionary: {dict_val}")

# Dictionary to Tuple
print("\nDictionary to Tuple:")
dict_val = {'x': 10, 'y': 20}
tuple_val = tuple(dict_val.items())  # Convert dictionary items to tuple of tuples
print(f"Dictionary {dict_val} to Tuple: {tuple_val}")
