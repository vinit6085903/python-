# Getting input from the user
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# Arithmetic Operators
print("\nArithmetic Operators:")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

# Comparison Operators
print("\nComparison Operators:")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# Logical Operators
print("\nLogical Operators:")
print(f"a > 0 and b > 0: {a > 0 and b > 0}")
print(f"a > 0 or b > 0: {a > 0 or b > 0}")
print(f"not (a > 0): {not (a > 0)}")

# Bitwise Operators
print("\nBitwise Operators:")
print(f"a & b = {a & b}")
print(f"a | b = {a | b}")
print(f"a ^ b = {a ^ b}")
print(f"~a = {~a}")
print(f"a << 1 = {a << 1}")
print(f"a >> 1 = {a >> 1}")

# Assignment Operators
print("\nAssignment Operators:")
c = a
print(f"c = a: c = {c}")
c += b
print(f"c += b: c = {c}")
c -= b
print(f"c -= b: c = {c}")
c *= b
print(f"c *= b: c = {c}")
c /= b
print(f"c /= b: c = {c}")
c //= b
print(f"c //= b: c = {c}")
c %= b
print(f"c %= b: c = {c}")
c **= b
print(f"c **= b: c = {c}")

# Membership Operators
lst = [a, b, a + b]
print("\nMembership Operators:")
print(f"a in lst: {a in lst}")
print(f"b in lst: {b in lst}")
print(f"a + b in lst: {a + b in lst}")

# Identity Operators
print("\nIdentity Operators:")
print(f"a is b: {a is b}")
print(f"a is not b: {a is not b}")
