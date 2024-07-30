# Getting input from the user
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# Basic if-else
print("\nBasic if-else:")
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is not greater than {b}")

# Nested if-else
print("\nNested if-else:")
if a > 0:
    if b > 0:
        print(f"Both {a} and {b} are positive numbers")
    else:
        print(f"{a} is positive, but {b} is not")
else:
    if b > 0:
        print(f"{a} is not positive, but {b} is")
    else:
        print(f"Neither {a} nor {b} is positive")

# Elif Example
print("\nElif Example:")
if a == b:
    print(f"{a} is equal to {b}")
elif a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than {b}")

# Multiple Conditions
print("\nMultiple Conditions:")
if a > 0 and b > 0:
    print(f"Both {a} and {b} are positive numbers")
elif a > 0 or b > 0:
    print(f"At least one of {a} or {b} is positive")
else:
    print(f"Neither {a} nor {b} is positive")

# Conditional Expressions (Ternary Operator)
print("\nConditional Expression (Ternary Operator):")
result = "a is greater" if a > b else "b is greater or equal"
print(result)

# Example of using a function with if-else
def categorize_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print("\nCategorize Number:")
print(f"{a} is {categorize_number(a)}")
print(f"{b} is {categorize_number(b)}")
