def grade(module_IN0005, module_IN0008, module_MA0004, module_b):
    average_grade = (module_IN0005 + module_IN0008 + module_MA0004 + module_b) / 4
    if student_type == 1:
        if average_grade >= 50:
            return ("Congratulations you can now proceed to Stage 1")
        elif average_grade < 50:
            return ("Sorry you cannot progress to Stage 1")
    elif student_type == 2:
        if average_grade >= 60:
            return ("Congratulations you can now proceed to Stage 1")
        elif average_grade < 60:
            return ("Sorry you cannot progress to Stage 1")

student_type = int(input("""What type of student are you?
- (2 = computer science, 1 = maths):\n"""))

b = input("What is your non-common module called?\n")

module_IN0005 = float(input("Type your grade for module IN0005 (give grade as percentage):\n"))
module_IN0008 = float(input("Type your grade for module IN0008 (give grade as percentage):\n"))
module_MA0004 = float(input("Type your grade for module MA0004 (give grade as percentage):\n"))
module_b = float(input("Type your grade for module {} (give grade as percentage) :\n".format(b)))

print(grade(module_IN0005, module_IN0008, module_MA0004, module_b))
        
