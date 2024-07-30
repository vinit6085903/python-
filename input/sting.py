# String Declaration
string1 = "Hello, World!"
string2 = 'Python Programming'
string3 = """This is a multi-line string
spanning multiple lines."""
string4 = '''Another example
of a multi-line string.'''

# String Concatenation
print("\nString Concatenation:")
concat_string = string1 + " " + string2
print(concat_string)

# String Repetition
print("\nString Repetition:")
repeat_string = string1 * 2
print(repeat_string)

# Accessing Characters in a String
print("\nAccessing Characters in a String:")
print(f"First character: {string1[0]}")
print(f"Last character: {string1[-1]}")

# Slicing Strings
print("\nSlicing Strings:")
print(f"First 5 characters: {string1[:5]}")
print(f"Characters from index 7 to 12: {string1[7:13]}")
print(f"Every second character: {string1[::2]}")

# String Length
print("\nString Length:")
print(f"Length of string1: {len(string1)}")

# String Methods
print("\nString Methods:")
print(f"Lowercase: {string1.lower()}")
print(f"Uppercase: {string1.upper()}")
print(f"Title case: {string1.title()}")
print(f"Capitalized: {string1.capitalize()}")
print(f"Strip whitespace: {'   Hello   '.strip()}")
print(f"Replace 'World' with 'Python': {string1.replace('World', 'Python')}")
print(f"Find 'World': {string1.find('World')}")
print(f"Find 'Python': {string1.find('Python')}")
print(f"Check if string1 starts with 'Hello': {string1.startswith('Hello')}")
print(f"Check if string1 ends with 'World!': {string1.endswith('World!')}")
print(f"Split string1 by ',': {string1.split(',')}")
print(f"Join list of strings: {', '.join(['Hello', 'Python', 'World'])}")

# String Formatting
print("\nString Formatting:")
name = "Alice"
age = 30
print(f"Formatted using f-strings: {name} is {age} years old.")
print("Formatted using format method: {} is {} years old.".format(name, age))
print("Formatted using % operator: %s is %d years old." % (name, age))

# Escaping Characters
print("\nEscaping Characters:")
escaped_string = "He said, \"Python is awesome!\""
print(escaped_string)

# Checking String Properties
print("\nChecking String Properties:")
print(f"Is 'hello' a digit? {'hello'.isdigit()}")
print(f"Is '12345' a digit? {'12345'.isdigit()}")
print(f"Is 'hello' alphabetic? {'hello'.isalpha()}")
print(f"Is 'hello123' alphanumeric? {'hello123'.isalnum()}")

# Multiline Strings
print("\nMultiline Strings:")
print(string3)
print(string4)

# Raw Strings (useful for regular expressions)
print("\nRaw Strings:")
raw_string = r"C:\Users\Name\Documents\file.txt"
print(raw_string)

# String Interpolation with Old-Style %
print("\nString Interpolation with Old-Style %:")
print("Name: %s, Age: %d" % (name, age))

# String Alignment
print("\nString Alignment:")
print(f"Left aligned: {'Hello'.ljust(10, '-')}")
print(f"Right aligned: {'Hello'.rjust(10, '-')}")
print(f"Center aligned: {'Hello'.center(10, '-')}")
