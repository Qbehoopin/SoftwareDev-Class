# Pseudocode: Calculate the average of three test scores

# Input: Get three test scores from the user
# score1 = read score 1
# score2 = read score 2
# score3 = read score 3

# Process: Calculate the average
# sum_of_scores = score1 + score2 + score3
# average = sum_of_scores / 3

# Output: Display the average
# print average

# Actual Implementation:
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))

average = (score1 + score2 + score3) / 3

print(f"The average of the three test scores is: {average}")