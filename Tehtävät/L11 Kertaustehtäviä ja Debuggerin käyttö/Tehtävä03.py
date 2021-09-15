inpt = input("Enter student name:")
student_names = ""
student_count = 0
if inpt != "":
    student_count += 1
    student_names += inpt
    while inpt != "":
        inpt = input("Enter student name:")
        if inpt == "":
            break
        else:
            student_names += ", "
            student_names += inpt
            student_count += 1
print("Student count:",student_count)
print(student_names)
