# CurrentTemp in Fernheit
# This program prompts the user to enter the current temperature in Fahrenheit
# and provides feedback based on the temperature range.

temperature = float(input("Enter the current temperature (in °F): "))

if temperature >= 90:
    print("It’s hot outside!")
elif 70 <= temperature <= 89:
    print("It’s warm outside!")
elif 50 <= temperature <= 69:
    print("It’s cool outside!")
else:
    print("It’s cold outside!")