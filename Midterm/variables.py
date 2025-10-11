# Program to calculate average of 3 test scores and print letter grade

# Get test scores from user
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))

# Calculate average
average = (score1 + score2 + score3) / 3

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print results
print(f"Average score: {average:.2f}")
print(f"Letter grade: {grade}")