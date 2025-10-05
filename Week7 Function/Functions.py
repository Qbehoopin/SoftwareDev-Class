# What is a function? 
# A function is a block of code that only runs when it is called to do a specific task.
# You can pass data, known as parameters, into a function.
# It can be reused multiple times without rewriting the code.
# You can use functions to make your code more organized, modular, and easier to read.

# Why use functions?
# 1. Reusability: You can call the same function multiple times without rewriting the code.
# 2. Modularity: Functions allow you to break down complex problems into smaller, manageable parts.
# 3. Readability: Functions can make your code more organized and easier to understand.
# 4. Maintainability: If you need to make changes, you can do so in one place (the function definition) rather than throughout your code.

# Avoid repetition: If you find yourself writing the same code multiple times, consider creating a function to encapsulate that code.
# Break problems into smaller parts: If a task can be divided into smaller subtasks, create functions for each subtask.
# Make programs easier to maintain: If you anticipate that a piece of code may need to be updated or modified in the future, encapsulate it in a function.

# Defining a function
# Syntax:
# def function_name(parameters):
#     # code block
#     return value  # optional

# Example:
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # Output: Hello, Alice!

# calling a function
greet("Bob")    # Output: Hello, Bob!

# Parameters (Single and Multiple)
# Function can take input values, known as parameters.
# Parameters are specified within the parentheses in the function definition.   
def greet_user(username):
    print(f"Welcome, {username}!")
greet_user("Charlie")  # Output: Welcome, Charlie!


# Functions can have more than one parameter.
def add(a, b):
    return a + b    
result = add(3, 5)
print(result)  # Output: 8

# Return Values
# Functions can return values using the return statement.
def square(x):
    return x * x
result = square(4)
print(result)  # Output: 16 
# If a function does not have a return statement, it returns None by default.
def no_return():
    print("This function does not return anything.")
result = no_return()  # Output: This function does not return anything.
print(result)  # Output: None

# common mistakes
# Forgetting parentheses when calling a function
# missing indentation
# Not providing all required parameters
# Using the wrong number of arguments
# Forgetting the return statement when needed
# Using mutable default arguments

