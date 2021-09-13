score = int(input("Point ammount for grading: "))

if score >= 0 and score < 2:
    print("Grade: 0")
elif score > 1 and score < 4:
    print("Grade: 1")
elif score > 3 and score < 6:
    print("Grade: 2")
elif score > 5 and score < 8:
    print("Grade: 3")
elif score > 7 and score < 10:
    print("Grade: 4")
elif score > 9 and score < 13:
    print("Grade: 5")
else:
    print("Outside Parameters")