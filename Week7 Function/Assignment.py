# 1.	A function with no parameters (example: prints a welcome message).
def welcome_message():
    print("Welcome to the Python programming world, by Q. Johnson!")
welcome_message()

# 2.	A function with one parameter (example: greets a person by name). 
def greet_person(name):
    print(f"Hello, {name}! Nice to meet you. Welcome to Q. Johnson's Python class.")
greet_person("Professor Taylor")

# 3.	A function with two parameters that returns a value (example: multiplies two numbers and prints the result). 
def multiply_and_print(num1, num2):
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")
    return result
multiply_and_print(652, 77)     
