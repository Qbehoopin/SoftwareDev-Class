Grade = float(input("Enter your grade: "))
if 90 <= Grade <= 100:
    print("Your grade is A, Excellent")
elif 80 <= Grade < 90:
    print("Your grade is B, Very Good")
elif 70 <= Grade < 80:
    print("Your grade is C, Good")
elif 60 <= Grade < 70:
    print("Your grade is F, Fail, You need to retake the course")
elif 0 <= Grade < 60:
    print("Your grade is F, Fail, You need to retake the course")

# this is a grade evaluation program