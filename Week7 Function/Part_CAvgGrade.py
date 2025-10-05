def grade_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    

# Example call
print(grade_average(85, 90, 80))
