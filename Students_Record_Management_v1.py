students = []


def add_student(students):
    num = get_integer("(How many students record would you like to add?): ")
    for i in range(num):
        name = input("Enter Name: ")
        age = get_integer("Enter age: ")
        grades = get_grades("Enter Grades: ")

        student = {
            "id": get_nxt_ID(students),
            "name": name,
            "age": age,
            "grades": grades,
        }

        students.append(student)

        print("Student record added successfully!")


def view_students(students):
    if not students:
        print("Student Record is Empty.")
        return

    print(" ID | Name    | Age | Grades ")
    for student in students:
        print(
            f"{student['id']} - {student['name']} - {student['age']} - {student['grades']}"
        )


def search_student(students):
    if not students:
        print("Student Record is Empty.")
        return
    s_id = get_integer("Enter Student ID: ")
    found = False
    for student in students:
        if student["id"] == s_id:
            print("Student Record:")
            print(
                f"{student['id']} - {student['name']} - {student['age']} - {student['grades']}"
            )
            found = True
            break
    # for s in students:             //Later will Improve this feature by adding option for searching by name and ID
    #     if s["name"].lower() == s_name.lower():
    #         print("STUDENT RECORD:")
    #         print(f" {s['name']} - {s['age']} - {s['grades']}")
    #         found = True
    #         break

    if not found:
        print("Student Record Not Found.")


def delete_student(students):
    if not students:
        print("Student Record is Empty.")
        return

    s_id = get_integer("Enter Student ID: ")

    for student in students:
        if student["id"] == s_id:
            students.remove(student)
            print("Student's Record Deleted Successfully..")
            break
    else:
        print("Student's record not found.")


def update_student(students):
    if not students:
        print("Student Record is Empty.")
        return

    s_id = get_integer("Enter Student ID: ")

    for student in students:
        if student["id"] == s_id:
            print("Current Record:")
            print(
                f"{student['id']} - {student['name']} - {student['age']} - {student['grades']}"
            )
            print("\nNow Update the Record: ")

            new_name = input("Enter new name: ")
            new_age = get_integer("Enter new age: ")
            new_grades = get_float("Enter new grades: ")

            student.update({"name": new_name, "age": new_age, "grades": new_grades})

            print("Student's Record Updated Successfully..")
            break
    else:
        print("Student's record not found.")


def top_student(students):
    if not students:
        print("Student Record is Empty.")
        return

    top = students[0]
    for student in students:
        if student["grades"] > top["grades"]:

            top = student

    print(f"{top['id']} - {top['name']} - {top['age']} - {top['grades']}")


def average_grades(students):
    if not students:
        print("Student Record is Empty.")
        return

    grades_sum = 0
    count = 0
    for student in students:
        if student["grades"] >= 0:
            grades_sum += student["grades"]
            count += 1

    avg_grades = grades_sum / count
    print(f"Average grades: {avg_grades:.2f}")


# File Handling *******************************************************************************


def save_data(students):
    file = open("record.txt", "w")

    for student in students:
        line = f"{student['id']},{student['name']},{student['age']},{student['grades']}"
        file.write(line)
        file.write("\n")

    file.close()


def load_data(students):
    try:
        file = open("record.txt", "r")

        for line in file:
            line = line.strip()
            parts = line.split(",")
            student = {
                "id": int(parts[0]),
                "name": parts[1],
                "age": int(parts[2]),
                "grades": float(parts[3]),
            }
            students.append(student)
        print("File loaded successfully :)")
        file.close()
    except FileNotFoundError:
        print("No saved records found. Starting with an empty database.")


# Helper Functions ****************************************************************************


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid Input :( -> Please enter a number.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid Input :( -> Please enter a number.")


def get_grades(prompt):
    while True:
        value = get_float(prompt)
        if value >= 0 and value <= 100:
            return value
        print("Grades must be between 0 and 100.")


def get_nxt_ID(students):

    max_id = 0
    for student in students:
        if student["id"] > max_id:
            max_id = student["id"]

    return max_id + 1


load_data(students)  #  Automatic Data Loading


while True:  #  Main Menu

    print("--- Student Record Management ---")
    print("1. Add Student Record.")
    print("2. View All Students Record.")
    print("3. Search for a Student record.")
    print("4. Show Top Student.")
    print("5. Show average grades.")
    print("6. Delete Student's record.")
    print("7. Update Student's record.")
    print("0. Exit System.")

    choice = get_integer("Enter Number(0 - 7): ")

    match choice:
        case 1:
            add_student(students)

        case 2:
            view_students(students)

        case 3:
            search_student(students)

        case 4:
            top_student(students)

        case 5:
            average_grades(students)

        case 6:
            delete_student(students)

        case 7:
            update_student(students)

        case 0:
            save_data(students)
            break  #  Exit ;)
