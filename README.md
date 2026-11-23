[README.md](https://github.com/user-attachments/files/35268262/README.md)
# Student Management System

A beginner-friendly, command-line **Student Management System** built with Python. It provides a simple way to register, view, search, update, and delete student records, with persistent local storage using JSON.

This project was created to practise core Python concepts and build a complete, usable application.

## Features

- **Register students** with their name, age, and course.
- **View all students** in a numbered list.
- **Search students** by name (case-insensitive).
- **Update student information**, including name, age, and course.
- **Delete students** with a confirmation prompt.
- **Save records automatically** in a local `students.json` file.
- **Load saved records** when the program starts again.
- **Validate user input**, including ages, blank fields, and duplicate names.
- **Handle missing or invalid JSON files** without silently overwriting existing records.

## Tech Stack

- **Language:** Python 3
- **Data storage:** JSON (Python standard library)
- **Interface:** Command-line / terminal
- **Dependencies:** None beyond Python's standard library

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Muhammedsuleiman/student-management-system.git
cd student-management-system
```

> If your GitHub repository has a different name, use its actual clone URL instead.

### 2. Run the application

Make sure Python 3 is installed, then run:

```bash
python main.py
```

On some systems, you may need `python3 main.py` or `py main.py` instead.

### 3. Use the menu

```text
========== MAIN MENU ==========
1. Register a Student
2. View All Students
3. Search for a Student
4. Update Student Information
5. Delete a Student
6. Exit
```

Enter a number from 1 to 6 and follow the prompts.

## How Data Storage Works

The application automatically creates `students.json` in the same folder as `main.py` after the first successful registration.

Example record:

```json
[
  {
    "name": "Amina Yusuf",
    "age": 21,
    "course": "Computer Science"
  }
]
```

When you restart the application, previously saved records are loaded automatically. If the JSON file is damaged, the program stops rather than replacing the existing data.

**Privacy note:** `students.json` can contain personal information. Avoid committing real student records to a public GitHub repository. You can add `students.json` to `.gitignore` and use fictional records when demonstrating the project.

## Project Structure

```text
student-management-system/
├── main.py           # Main Python application
├── README.md         # Project documentation
└── students.json     # Created automatically at runtime (keep private)
```

## Testing

The project has been exercised using command-line scenarios covering:

| Scenario | Expected result |
| --- | --- |
| Register a student | Record is added and saved |
| View and search | Existing records are displayed and found |
| Update a student | Changes are saved |
| Delete or cancel deletion | Confirmation is respected |
| Enter invalid input | Invalid values are rejected |
| Restart the application | Saved records are loaded |
| Load damaged JSON | Program stops to protect the file |

You can repeat these checks manually after cloning the repository.

## What I Learned

- Defining and calling Python functions
- Using lists and dictionaries to organise records
- Building menus with `while` loops and conditional statements
- Validating input with `try` / `except`
- Reading and writing JSON files
- Handling file errors and protecting saved data
- Structuring a small Python application from start to finish

## Future Improvements

Potential next steps include unique student IDs, additional search filters, automated unit tests, and a graphical interface.

## Author

**Muhammad Suleiman**

GitHub: [@Muhammedsuleiman](https://github.com/Muhammedsuleiman)

---

*Built as a practical Python learning project.*
