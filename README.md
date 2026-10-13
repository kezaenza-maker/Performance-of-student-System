[second chance.py](https://github.com/user-attachments/files/33397587/second.chance.py)

def enter_student():
    print("\n===== ENTER STUDENT INFORMATION =====")

    # Variables and data types
    name = input("Enter student name: ")
    student_class = input("Enter student class: ")

    subjects = ["Mathematics", "English", "Programming",
                "Database", "Networking"]

    marks = []

    # for loop
    for subject in subjects:
        mark = int(input("Enter " + subject + " mark: "))

        # while loop: check that the mark is valid
        while mark < 0 or mark > 100:
            print("Invalid mark. Enter a mark from 0 to 100.")
            mark = int(input("Enter " + subject + " mark: "))

        marks.append(mark)

    # Calculate total using operators and a for loop
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(subjects)

    # if, elif and else
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n===== STUDENT RESULTS =====")
    print("Student name:", name)
    print("Student class:", student_class)

    for number in range(len(subjects)):
        print(subjects[number] + ":", marks[number])

    print("Total marks:", total, "/ 500")
    print("Average:", average)
    print("Grade:", grade)

    return name, student_class, marks, total


def main():
    # while loop: keep showing the menu
    while True:
        print("\n===== STUDENT PERFORMANCE SYSTEM =====")
        print("1. Enter student information")
        print("2. Exit")

        choice = input("Choose an option: ")

        # match statement
        match choice:
            case "1":
                enter_student()

            case "2":
                print("Thank you for using the system!")
                break

            case _:
                print("Invalid choice. Please choose 1 or 2.")


# Call the main function
main()


