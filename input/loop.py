# For Loop Examples

# Loop through a range of numbers
print("For Loop with range():")
for i in range(5):  # from 0 to 4
    print(i)

# Loop through a list
print("\nFor Loop with a list:")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Loop through a dictionary
print("\nFor Loop with a dictionary:")
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")

# Loop through a string
print("\nFor Loop with a string:")
for char in "Hello":
    print(char)

# While Loop Examples

# Basic while loop
print("\nBasic While Loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with break statement
print("\nWhile Loop with break statement:")
count = 0
while True:
    if count == 3:
        break
    print(count)
    count += 1

# While loop with continue statement
print("\nWhile Loop with continue statement:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

# Nested Loops

# Nested for loops
print("\nNested For Loops:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Nested while loops
print("\nNested While Loops:")
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Loop Control Statements

# Loop with else
print("\nLoop with else:")
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Infinite loop with a break condition
print("\nInfinite loop with break condition:")
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

# Using a function with loops
def print_table(n):
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Print multiplication table for 5
print_table(5)
