
# ==========================================
# STUDENT MANAGEMENT SYSTEM - PHASES 1 TO 7
# ==========================================

import json
from pathlib import Path


# ==========================================
# FILE STORAGE CONFIGURATION
# ==========================================

# Save students.json in the same folder as main.py
DATA_FILE = Path(__file__).resolve().parent / "students.json"


# ==========================================
# PHASE 7 - LOAD SAVED STUDENTS
# ==========================================

def load_students():

    # If the file does not exist, start with an empty list
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Make sure the saved data is a list
        if not isinstance(data, list):
            raise ValueError("Student data must be a list.")

        # Validate every saved student
        for student in data:

            if not isinstance(student, dict):
                raise ValueError("Invalid student record.")

            if not isinstance(student.get("name"), str):
                raise ValueError("Invalid student name.")

            if not student["name"].strip():
                raise ValueError("Student name cannot be empty.")

            if type(student.get("age")) is not int or student["age"] <= 0:
                raise ValueError("Invalid student age.")

            if not isinstance(student.get("course"), str):
                raise ValueError("Invalid student course.")

        return data

    except (json.JSONDecodeError, OSError, ValueError) as error:

        print("\nError loading student records:", error)
        print("Please check students.json before continuing.")

        return None


# ==========================================
# PHASE 7 - SAVE STUDENTS
# ==========================================

def save_students():

    # Use a temporary file to protect existing records
    temporary_file = DATA_FILE.with_suffix(".tmp")

    try:
        with open(temporary_file, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4, ensure_ascii=False)

        # Replace the old file after saving successfully
        temporary_file.replace(DATA_FILE)

        return True

    except OSError as error:

        print("\nError saving student records:", error)
        return False


# ==========================================
# VALIDATE STUDENT AGE
# ==========================================

def read_age(prompt):

    while True:

        try:
            age = int(input(prompt))

            if age > 0:
                return age

            print("Age must be greater than zero.")

        except ValueError:
            print("Please enter a whole number for age.")


# ==========================================
# FIND A STUDENT BY NAME
# ==========================================

def find_student(search_name):

    for student in students:

        if student["name"].strip().lower() == search_name.strip().lower():
            return student

    return None


# ==========================================
# DISPLAY STUDENT INFORMATION
# ==========================================

def display_student(student):

    print("Student Name:", student["name"])
    print("Student Age:", student["age"])
    print("Student Course:", student["course"])


# ==========================================
# PHASE 2 - REGISTER STUDENT
# ==========================================

def register_student():

    print("\n========== REGISTER STUDENT ==========")

    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty.")
        return

    # Prevent duplicate names
    if find_student(student_name) is not None:
        print("A student with this name already exists.")
        return

    age = read_age("Enter student age: ")
    course = input("Enter student course: ").strip()

    if not course:
        print("Student course cannot be empty.")
        return

    # Create the student's dictionary
    student = {
        "name": student_name,
        "age": age,
        "course": course
    }

    # Add student to the list
    students.append(student)

    # Save the updated student list
    if save_students():

        print("\nStudent registered successfully!")
        display_student(student)

    else:

        # Undo registration if saving fails
        students.remove(student)
        print("Registration was not saved.")


# ==========================================
# PHASE 3 - VIEW ALL STUDENTS
# ==========================================

def view_students():

    print("\n========== REGISTERED STUDENTS ==========")

    if not students:
        print("No students registered yet!")
        return

    # Display all students with numbers
    for number, student in enumerate(students, start=1):

        print("\nStudent Number:", number)
        display_student(student)
        print("----------------------------------------")


# ==========================================
# PHASE 4 - SEARCH STUDENT
# ==========================================

def search_student():

    print("\n========== SEARCH STUDENT ==========")

    search_name = input("Enter student name to search: ")

    student = find_student(search_name)

    if student is None:
        print("Student not found!")

    else:
        print("\nStudent Found!")
        display_student(student)


# ==========================================
# PHASE 5 - UPDATE STUDENT INFORMATION
# ==========================================

def update_student():

    print("\n========== UPDATE STUDENT ==========")

    search_name = input("Enter student name to update: ")

    student = find_student(search_name)

    if student is None:
        print("Student not found!")
        return

    print("\nStudent Found!")
    display_student(student)

    print("\nWhat would you like to update?")
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Course")
    print("4. Cancel")

    option = input("Enter your choice (1-4): ")

    # Keep original data in case saving fails
    original_student = student.copy()

    if option == "1":

        new_name = input("Enter new name: ").strip()

        if not new_name:
            print("Name cannot be empty.")
            return

        existing_student = find_student(new_name)

        if existing_student is not None and existing_student is not student:
            print("Another student already has this name.")
            return

        student["name"] = new_name

    elif option == "2":

        student["age"] = read_age("Enter new age: ")

    elif option == "3":

        new_course = input("Enter new course: ").strip()

        if not new_course:
            print("Course cannot be empty.")
            return

        student["course"] = new_course

    elif option == "4":

        print("Update cancelled.")
        return

    else:

        print("Invalid update option.")
        return

    # Save the updated information
    if save_students():

        print("\nStudent updated successfully!")
        display_student(student)

    else:

        # Restore the original information if saving fails
        student.update(original_student)
        print("Update was not saved.")


# ==========================================
# PHASE 6 - DELETE STUDENT
# ==========================================

def delete_student():

    print("\n========== DELETE STUDENT ==========")

    search_name = input("Enter student name to delete: ")

    student = find_student(search_name)

    if student is None:
        print("Student not found!")
        return

    print("\nStudent Found!")
    display_student(student)

    # Ask before deleting
    confirm = input(
        "\nAre you sure you want to delete this student? (yes/no): "
    )

    if confirm.strip().lower() != "yes":
        print("Deletion cancelled.")
        return

    # Remember the student's position
    student_index = students.index(student)

    # Remove the student
    students.pop(student_index)

    if save_students():

        print("\nStudent deleted successfully!")

    else:

        # Restore the student if saving fails
        students.insert(student_index, student)
        print("Deletion was not saved.")


# ==========================================
# PHASE 1 - MAIN MENU
# ==========================================

def choice(name):

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Register a Student")
        print("2. View All Students")
        print("3. Search for a Student")
        print("4. Update Student Information")
        print("5. Delete a Student")
        print("6. Exit")

        option = input("Enter your choice (1-6): ").strip()

        if option == "1":
            register_student()

        elif option == "2":
            view_students()

        elif option == "3":
            search_student()

        elif option == "4":
            update_student()

        elif option == "5":
            delete_student()

        elif option == "6":

            print("\nGoodbye,", name + "!")
            print("Thank you for using the Student Management System!")
            break

        else:
            print("\nInvalid option. Please try again.")


# ==========================================
# START APPLICATION
# ==========================================

def main():

    print("================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    global students

    # Load saved student records
    students = load_students()

    # Stop if the saved data cannot be loaded safely
    if students is None:
        print("Application stopped to protect your saved records.")
        return

    # Welcome the user
    name = input("What is your name? ").strip()

    print(
        "Hello,",
        name + "!",
        "Welcome to the Student Management System!"
    )

    # Start the main menu and pass the user's name
    choice(name)


# ==========================================
# RUN THE PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
