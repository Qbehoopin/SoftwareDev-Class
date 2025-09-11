# Simple Calculator for Two Numbers
def main():
	# ...existing code...
	try:
		num1 = int(input('Enter first number: '))
		num2 = int(input('Enter second number: '))
	except ValueError:
		print('Invalid input. Please enter integer values.')
		return

	print('Addition:', num1 + num2)
	print('Subtraction:', num1 - num2)
	print('Multiplication:', num1 * num2)
	try:
		print('Division:', num1 / num2)
	except ZeroDivisionError:
		print('Division: Error (division by zero)')
	try:
		print('Modulus:', num1 % num2)
	except ZeroDivisionError:
		print('Modulus: Error (modulus by zero)')
	try:
		print('Floor Division:', num1 // num2)
	except ZeroDivisionError:
		print('Floor Division: Error (floor division by zero)')
	print('Exponentiation:', num1 ** num2)

if __name__ == "__main__":
	main()
