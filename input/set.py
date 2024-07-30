# Set Declaration
print("Set Declaration:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2, 3, 3, 3}  # Duplicates are ignored
print("set1:", set1)
print("set2:", set2)
print("set3 (with duplicates removed):", set3)

# Adding Elements
print("\nAdding Elements:")
set1.add(6)
print("After add(6):", set1)
set1.update([7, 8, 9])  # Add multiple elements
print("After update([7, 8, 9]):", set1)

# Removing Elements
print("\nRemoving Elements:")
set1.remove(9)  # Remove specific element; raises KeyError if not present
print("After remove(9):", set1)
set1.discard(10)  # Remove element if present; does nothing if not present
print("After discard(10):", set1)
popped_element = set1.pop()  # Remove and return an arbitrary element
print(f"Popped element: {popped_element}")
print("After pop():", set1)
set1.clear()  # Remove all elements
print("After clear():", set1)

# Set Operations
print("\nSet Operations:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union (set1 | set2): {set1 | set2}")
print(f"Intersection (set1 & set2): {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference (set1 ^ set2): {set1 ^ set2}")

# Set Methods
print("\nSet Methods:")
print(f"Length of set1: {len(set1)}")
print(f"Check if set2 is subset of set1: {set2.issubset(set1)}")
print(f"Check if set1 is superset of set2: {set1.issuperset(set2)}")
print(f"Disjoint sets (no common elements): {set1.isdisjoint(set2)}")

# Set Comprehensions
print("\nSet Comprehensions:")
squares = {x**2 for x in range(6)}
print("Squares of numbers from 0 to 5:", squares)
even_numbers = {x for x in range(10) if x % 2 == 0}
print("Even numbers from 0 to 9:", even_numbers)

# Frozen Set
print("\nFrozen Set:")
frozen_set1 = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", frozen_set1)

# Note: Frozen sets are immutable and do not support methods that modify the set
# For example:
# frozen_set1.add(6)  # This will raise an AttributeError
