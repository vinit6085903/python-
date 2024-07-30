# Basic Function
def greet(name):
    """This function greets the person with the given name."""
    print(f"Hello, {name}!")

# Calling the Function
greet("Alice")
# Function with Return Value
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Calling the Function and Using Return Value
result = add(5, 3)
print(f"Sum: {result}")
# Function with Default Parameter
def power(base, exponent=2):
    """This function returns the base raised to the exponent."""
    return base ** exponent

# Calling the Function with and without Default Parameter
print(power(4))         # Uses default exponent (2)
print(power(4, 3))      # Uses provided exponent (3)
# Function with Keyword Arguments
def describe_person(name, age, city):
    """This function describes a person with name, age, and city."""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Calling the Function with Keyword Arguments
describe_person(age=25, name="Bob", city="Los Angeles")
# Function with Variable-Length Arguments
def summarize(*args):
    """This function returns the sum of all provided arguments."""
    return sum(args)

# Calling the Function with Different Number of Arguments
print(summarize(1, 2, 3))
print(summarize(10, 20, 30, 40, 50))
# Lambda Function
add = lambda x, y: x + y

# Calling the Lambda Function
print(add(10, 5))
# Function with Keyword-Only Arguments
def describe_person(name, *, age, city):
    """This function requires 'age' and 'city' to be passed as keyword arguments."""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Calling the Function with Keyword-Only Arguments
describe_person("Charlie", age=30, city="San Francisco")
# Function with Nested Function
def outer_function(x):
    """Outer function with an inner function."""
    def inner_function(y):
        """Inner function."""
        return y * y
    return inner_function(x) + x

# Calling the Outer Function
print(outer_function(3))
# Function with a Docstring
def multiply(a, b):
    """Returns the product of two numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The product of the two numbers.
    """
    return a * b

# Accessing the Docstring
print(multiply.__doc__)
# Function with Annotations
def divide(numerator: float, denominator: float) -> float:
    """Returns the result of dividing the numerator by the denominator."""
    return numerator / denominator

# Calling the Function
print(divide(10.0, 2.0))
# Recursive Function to Calculate Factorial
def factorial(n):
    """Returns the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the Recursive Function
print(factorial(5))
# Function with Closure
def make_multiplier(factor):
    """Returns a function that multiplies by the given factor."""
    def multiplier(number):
        return number * factor
    return multiplier

# Creating and Using a Closure
times_two = make_multiplier(2)
print(times_two(10))  # Output: 20
