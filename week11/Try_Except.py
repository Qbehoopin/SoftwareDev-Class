# Using Try and Except to Handle Errors
# The try and except blocks in Python are used to handle exceptions (errors) gracefully.
# This allows the program to continue running even if an error occurs.

# Example of using try and except
try:
    x = 10/0 # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
# You can also catch multiple types of exceptions

# Multiple except blocks
# Handle different exceptions separately
# Example: Handling both ZeroDivisionError and ValueError
try:
    num=int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")

# Finally block
# The finally block is optional and will always execute, regardless of whether an exception occurred or not
# Example of using finally
try:
    f= open('data.txt')
finally:
    f.close()
    print("File closed successfully.")  