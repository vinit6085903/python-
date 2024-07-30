# Tuple Declaration
print("Tuple Declaration:")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
tuple3 = (1, 'apple', 3.14, (1, 2, 3))
tuple4 = 1, 2, 3  # Tuple without parentheses
print("tuple1:", tuple1)
print("tuple2:", tuple2)
print("tuple3:", tuple3)
print("tuple4:", tuple4)

# Accessing Tuple Elements
print("\nAccessing Tuple Elements:")
print(f"First element of tuple1: {tuple1[0]}")
print(f"Last element of tuple2: {tuple2[-1]}")
print(f"Element at index 2 of tuple3: {tuple3[2]}")
print(f"Nested tuple in tuple3: {tuple3[3]}")

# Slicing Tuples
print("\nSlicing Tuples:")
print(f"First three elements of tuple1: {tuple1[:3]}")
print(f"Elements from index 2 to 4: {tuple1[2:5]}")
print(f"Every second element of tuple1: {tuple1[::2]}")

# Tuple Length
print("\nTuple Length:")
print(f"Length of tuple1: {len(tuple1)}")

# Tuple Methods
print("\nTuple Methods:")
print(f"Index of 3 in tuple1: {tuple1.index(3)}")
print(f"Count of 1 in tuple1: {tuple1.count(1)}")

# Concatenating Tuples
print("\nConcatenating Tuples:")
concat_tuple = tuple1 + tuple2
print("Concatenated tuple:", concat_tuple)

# Repeating Tuples
print("\nRepeating Tuples:")
repeat_tuple = tuple1 * 2
print("Repeated tuple:", repeat_tuple)

# Unpacking Tuples
print("\nUnpacking Tuples:")
a, b, c, d, e = tuple1
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

# Nested Tuples
print("\nNested Tuples:")
nested_tuple = (1, (2, 3), (4, (5, 6)))
print("Nested tuple:", nested_tuple)
print("Accessing element 5 in nested tuple:", nested_tuple[1][1])

# Tuple with Single Element
print("\nTuple with Single Element:")
single_element_tuple = (1,)
print("Single element tuple:", single_element_tuple)
print("Type of single_element_tuple:", type(single_element_tuple))

# Tuple Conversion
print("\nTuple Conversion:")
list_from_tuple = list(tuple1)
print("List from tuple1:", list_from_tuple)
tuple_from_list = tuple(list_from_tuple)
print("Tuple from list:", tuple_from_list)

# Tuple as Dictionary Keys
print("\nTuple as Dictionary Keys:")
dict_with_tuple_keys = {tuple1: 'values', ('a', 'b'): 'other values'}
print("Dictionary with tuple keys:", dict_with_tuple_keys)
