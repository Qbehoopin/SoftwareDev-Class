# Create a small program that prints all numbers from 1 to 50 using a loop and an if statement to check if the number is even or odd.
for num in range(1, 51):  # Loop through numbers 1 to 50
    if num % 2 == 0:  # Check if the number is even
        print(f"{num} is even")  # Print if the number is even
    else:
        print(f"{num} is odd")  # Print if the number is odd
# --- IGNORE ---