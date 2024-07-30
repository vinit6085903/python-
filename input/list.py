# List Declaration
print("List Declaration:")
list1 = [1, 2, 3, 4, 5]
list2 = ['apple', 'banana', 'cherry']
list3 = [1, 'apple', 3.14, [1, 2, 3]]
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

# Accessing List Elements
print("\nAccessing List Elements:")
print(f"First element of list1: {list1[0]}")
print(f"Last element of list2: {list2[-1]}")
print(f"Element at index 2 of list3: {list3[2]}")
print(f"Nested list in list3: {list3[3]}")

# Slicing Lists
print("\nSlicing Lists:")
print(f"First three elements of list1: {list1[:3]}")
print(f"Elements from index 2 to 4: {list1[2:5]}")
print(f"Every second element of list1: {list1[::2]}")

# Modifying Lists
print("\nModifying Lists:")
list1[1] = 10
print("Modified list1:", list1)

# Adding Elements
print("\nAdding Elements:")
list1.append(6)  # Add to the end
print("After append:", list1)
list1.insert(1, 7)  # Insert at a specific index
print("After insert:", list1)
list1.extend([8, 9])  # Extend the list by appending elements from another list
print("After extend:", list1)

# Removing Elements
print("\nRemoving Elements:")
list1.remove(10)  # Remove first occurrence of a value
print("After remove:", list1)
popped_element = list1.pop()  # Remove and return the last element
print(f"Popped element: {popped_element}")
print("After pop:", list1)
del list1[1]  # Remove element by index
print("After del:", list1)
list1.clear()  # Remove all elements
print("After clear:", list1)

# Copying Lists
print("\nCopying Lists:")
list1 = [1, 2, 3, 4, 5]
list_copy = list1.copy()  # Create a shallow copy of the list
print("Original list1:", list1)
print("Copied list_copy:", list_copy)

# List Methods
print("\nList Methods:")
print(f"Index of 4 in list1: {list1.index(4)}")
print(f"Count of 2 in list1: {list1.count(2)}")
list1.sort()  # Sort the list in ascending order
print("Sorted list1:", list1)
list1.reverse()  # Reverse the list
print("Reversed list1:", list1)

# List Comprehensions
print("\nList Comprehensions:")
squares = [x**2 for x in range(6)]
print("Squares of numbers from 0 to 5:", squares)
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers from 0 to 9:", even_numbers)

# Nested Lists
print("\nNested Lists:")
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)
print("Accessing element 4 in nested list:", nested_list[1][1])

# List Operations
print("\nList Operations:")
combined_list = list1 + [7, 8, 9]
print("Combined list:", combined_list)
repeated_list = [0] * 4
print("Repeated list:", repeated_list)
