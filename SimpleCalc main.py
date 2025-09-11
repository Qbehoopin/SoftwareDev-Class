# Simple Calculator for Two Numbers
def main():
	print("Simple Calculator for Two Numbers")
	try:
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
	except ValueError:
		print("Invalid input. Please enter numeric values.")
		return

	print("\nResults:")
	print(f"{num1} + {num2} = {num1 + num2}")
	print(f"{num1} - {num2} = {num1 - num2}")
	print(f"{num1} * {num2} = {num1 * num2}")
	try:
		print(f"{num1} / {num2} = {num1 / num2}")
	except ZeroDivisionError:
		print(f"{num1} / {num2} = Error (division by zero)")
	try:
		print(f"{num1} % {num2} = {num1 % num2}")
	except ZeroDivisionError:
		print(f"{num1} % {num2} = Error (modulus by zero)")
	try:
		print(f"{num1} // {num2} = {num1 // num2}")
	except ZeroDivisionError:
		print(f"{num1} // {num2} = Error (floor division by zero)")
	print(f"{num1} ** {num2} = {num1 ** num2}")

if __name__ == "__main__":
	main()
