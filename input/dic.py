# Dictionary Declaration
print("Dictionary Declaration:")
dict1 = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
dict2 = dict(name='Bob', age=25, city='Los Angeles')  # Another way to create dictionaries
print("dict1:", dict1)
print("dict2:", dict2)

# Accessing Values
print("\nAccessing Values:")
print(f"Name in dict1: {dict1['name']}")
print(f"City in dict2: {dict2.get('city')}")  # Using get() to avoid KeyError

# Adding and Updating Values
print("\nAdding and Updating Values:")
dict1['email'] = 'alice@example.com'  # Add a new key-value pair
print("After adding email:", dict1)
dict1['age'] = 31  # Update an existing value
print("After updating age:", dict1)

# Removing Values
print("\nRemoving Values:")
del dict1['email']  # Remove a specific key-value pair
print("After deleting email:", dict1)
popped_value = dict1.pop('city', 'Not Found')  # Remove and return the value of a specified key
print(f"Popped value (city): {popped_value}")
print("After pop:", dict1)
dict1.clear()  # Remove all items
print("After clear():", dict1)

# Dictionary Methods
print("\nDictionary Methods:")
dict1 = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(f"Keys: {dict1.keys()}")
print(f"Values: {dict1.values()}")
print(f"Items: {dict1.items()}")

# Copying Dictionaries
print("\nCopying Dictionaries:")
dict_copy = dict1.copy()  # Create a shallow copy
print("Original dict1:", dict1)
print("Copied dict_copy:", dict_copy)

# Dictionary Comprehensions
print("\nDictionary Comprehensions:")
squares = {x: x**2 for x in range(6)}
print("Squares dictionary:", squares)
even_numbers = {x: x*2 for x in range(5) if x % 2 == 0}
print("Even numbers dictionary:", even_numbers)

# Nested Dictionaries
print("\nNested Dictionaries:")
nested_dict = {
    'person': {
        'name': 'Alice',
        'age': 30
    },
    'address': {
        'city': 'New York',
        'zip': '10001'
    }
}
print("Nested dictionary:", nested_dict)
print(f"Person's name: {nested_dict['person']['name']}")
print(f"City: {nested_dict['address']['city']}")

# Dictionary with Tuple Keys
print("\nDictionary with Tuple Keys:")
dict_with_tuple_keys = {
    (1, 2): 'tuple1',
    (3, 4): 'tuple2'
}
print("Dictionary with tuple keys:", dict_with_tuple_keys)

# Iterating Over Dictionaries
print("\nIterating Over Dictionaries:")
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")

# Using defaultdict from collections
from collections import defaultdict

print("\nUsing defaultdict from collections:")
default_dict = defaultdict(int)
default_dict['a'] += 1
default_dict['b'] += 2
print("default_dict:", dict(default_dict))  # Convert to regular dict for printing

# Using Counter from collections
from collections import Counter

print("\nUsing Counter from collections:")
counter = Counter('abracadabra')
print("Counter:", counter)
print("Most common character:", counter.most_common(1))
