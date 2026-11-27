"""
P3: Student Record Manager
Name: Kenjimor Celestino
Section: IV-BSIT B
"""
print("-jjjk")
#python3 set1/p3/p3_record_manager.py

# students: a LIST that stores the names exactly as typed (for nice display).
# seen_names: a SET that stores the lowercase version of each name, used only
# to check quickly for duplicates.
students = []
seen_names = set()


def normalize(name):
    return " ".join(name.split()).lower()


def add_student():
    name = " ".join(input("Enter student name to add: ").split())
    if name == "":
        print("Name cannot be empty.")
        return

    key = normalize(name)
    if key in seen_names:
        print(f"'{name}' already exists. Duplicate not added.")
        return

    students.append(name.title())
    seen_names.add(key)
    print(f"'{name.title()}' was added.")


def remove_student():
    name = input("Enter student name to remove: ")
    key = normalize(name)

    if key not in seen_names:
        print(f"'{name.strip()}' was not found.")
        return

    for student in students:
        if normalize(student) == key:
            students.remove(student)
            break
    seen_names.remove(key)
    print(f"'{name.strip().title()}' was removed.")


def search_student():
    term = normalize(input("Enter name or part of a name to search: "))
    if term == "":
        print("Please type something to search.")
        return

    matches = [s for s in sorted(students, key=normalize) if term in normalize(s)]

    if not matches:
        print("No matching students found.")
        return

    print(f"\nFound {len(matches)} match(es):")
    for number, student in enumerate(matches, start=1):
        print(f"  {number}. {student}")


def display_students():
    if not students:
        print("No students in the list yet.")
        return

    print("\n--- Student List (A-Z) ---")
    for number, student in enumerate(sorted(students, key=normalize), start=1):
        print(f"{number}. {student}")
    print(f"Total students: {len(students)}")


def show_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Display all students")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()

# EXPLANATION:
# A list is an ordered collection that keeps items in the order they were added
# and allows duplicates, while a set is an unordered collection that cannot hold
# duplicates and can check "is this item in here?" very quickly. I used a list
# (students) to store the names so they can be displayed, numbered, and sorted
# alphabetically. I used a set (seen_names) to store the lowercase version of
# every name, so the program can instantly tell if a name already exists and
# prevent duplicates, even if it is typed as "kenji Celestino" or "Kenji      cELESTINO".