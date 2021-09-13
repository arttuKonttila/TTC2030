score = int(input("Point ammount for grading: "))

def calculate_grade(score):
    if score >= 0 and score < 2:
        return "Grade: 0"
    elif score > 1 and score < 4:
        return "Grade: 1"
    elif score > 3 and score < 6:
        return "Grade: 2"
    elif score > 5 and score < 8:
        return "Grade: 3"
    elif score > 7 and score < 10:
        return "Grade: 4"
    elif score > 9 and score < 13:
        return "Grade: 5"
    else:
        return "Outside Parameters"

final_grade = calculate_grade(score)
print(final_grade)