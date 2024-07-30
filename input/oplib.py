import operator as op

# Getting input from the user
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# Arithmetic Operators
print("\nArithmetic Operators:")
print(f"a + b = {op.add(a, b)}")
print(f"a - b = {op.sub(a, b)}")
print(f"a * b = {op.mul(a, b)}")
print(f"a / b = {op.truediv(a, b)}")
print(f"a // b = {op.floordiv(a, b)}")
print(f"a % b = {op.mod(a, b)}")
print(f"a ** b = {op.pow(a, b)}")

# Comparison Operators
print("\nComparison Operators:")
print(f"a == b: {op.eq(a, b)}")
print(f"a != b: {op.ne(a, b)}")
print(f"a > b: {op.gt(a, b)}")
print(f"a < b: {op.lt(a, b)}")
print(f"a >= b: {op.ge(a, b)}")
print(f"a <= b: {op.le(a, b)}")

# Logical Operators (Note: The `operator` module does not provide logical operators, but you can use `and`, `or`, `not` directly)
print("\nLogical Operators:")
print(f"a > 0 and b > 0: {op.and_(a > 0, b > 0)}")
print(f"a > 0 or b > 0: {op.or_(a > 0, b > 0)}")
print(f"not (a > 0): {op.not_(a > 0)}")

# Bitwise Operators
print("\nBitwise Operators:")
print(f"a & b = {op.and_(a, b)}")
print(f"a | b = {op.or_(a, b)}")
print(f"a ^ b = {op.xor(a, b)}")
print(f"~a = {op.inv(a)}")
print(f"a << 1 = {op.lshift(a, 1)}")
print(f"a >> 1 = {op.rshift(a, 1)}")

# Assignment Operators (The `operator` module does not directly provide assignment operators, but you can simulate them)
print("\nAssignment Operators:")
c = a
print(f"c = a: c = {c}")
c = op.add(c, b)
print(f"c += b: c = {c}")
c = op.sub(c, b)
print(f"c -= b: c = {c}")
c = op.mul(c, b)
print(f"c *= b: c = {c}")
c = op.truediv(c, b)
print(f"c /= b: c = {c}")
c = op.floordiv(c, b)
print(f"c //= b: c = {c}")
c = op.mod(c, b)
print(f"c %= b: c = {c}")
c = op.pow(c, b)
print(f"c **= b: c = {c}")

# Membership Operators (The `operator` module does not provide membership operators, but you can use `in` directly)
lst = [a, b, a + b]
print("\nMembership Operators:")
print(f"a in lst: {op.contains(lst, a)}")
print(f"b in lst: {op.contains(lst, b)}")
print(f"a + b in lst: {op.contains(lst, a + b)}")

# Identity Operators (The `operator` module does not provide identity operators, but you can use `is` directly)
print("\nIdentity Operators:")
print(f"a is b: {a is b}")
print(f"a is not b: {a is not b}")
