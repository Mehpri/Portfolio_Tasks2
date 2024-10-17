grade = int(input("Enter a grade between 0-100"))
if grade >= 80 and grade <= 100:
    print("Your grade is: A")
elif grade >= 60 and grade <= 79:
    print("Your grade is: B")
elif grade >= 50 and grade <= 59:
    print("Your grade is: C")
elif grade >= 40 and grade <= 49:
    print("Your grade is: D")
elif grade >= 0 and grade <= 39:
    print("Your grade: F")
elif grade > 100 or grade < 0:
    print("Grades must be between 0-100")
else:
    print("Please enter a number")