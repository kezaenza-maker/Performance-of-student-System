
def enter_student():
    print("===== ENTER STUDENT INFORMATION =====")

    name = input("Enter student name: ")
    student_class = input("Enter student class: ")

    print("Enter marks from 0 to 100.")

    subjects = 5

    for number in range(1, subjects + 1):
        print("You are entering mark number " + str(number))

    math = int(input("Enter Mathematics mark: "))
    english = int(input("Enter English mark: "))
    programming = int(input("Enter Programming mark: "))
    database = int(input("Enter Database mark: "))
    networking = int(input("Enter Networking mark: "))

    if (math >= 0 and math <= 100
        and english >= 0 and english <= 100
        and programming >= 0 and programming <= 100
        and database >= 0 and database <= 100
        and networking >= 0 and networking <= 100):
        print("Student information saved.")
    else:
        print("Invalid marks. Marks must be from 0 to 100.")

    return name, student_class, math, english, programming, database, networking


student = enter_student()

