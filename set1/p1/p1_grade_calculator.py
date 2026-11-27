"""
Name: KENJIMOR CELESTINO
Section: IV-BSIT B
Activity: P1 - Grade Calculator
-jjjk
"""

#python3 set1/p1/p1_grade_calculator.py

print("-jjjk")
PASSING_AVERAGE = 75
grades = []


# ----- Computing functions (they only return, they do not print) -----
def compute_average(grade_list):
    total = sum(grade_list)
    return total / len(grade_list)


def get_highest(grade_list):
    return max(grade_list)


def get_lowest(grade_list):
    return min(grade_list)


def get_status(grade_list):
    if compute_average(grade_list) >= PASSING_AVERAGE:
        return "PASSED"
    return "FAILED"


# ----- Input and menu functions -----
def get_valid_grade(prompt):
    # keeps asking until the grade is a number from 0 to 100
    while True:
        text = input(prompt).strip()

        # remove one dot first, then check if the rest are only digits
        if not text.replace(".", "", 1).isdecimal():
            print("Invalid input. Please enter a number.")
            continue

        grade = float(text)
        if 0 <= grade <= 100:
            return grade
        print("Invalid grade. It must be from 0 to 100.")


def enter_grades(grade_list):
    grade_list.clear()
    print("\nEnter the grades one at a time.")

    while True:
        grade = get_valid_grade(f"Grade #{len(grade_list) + 1}: ")
        grade_list.append(grade)

        more = input("Add another grade? (y/n): ").strip().lower()
        while more not in ("y", "n"):
            more = input("Please type y or n: ").strip().lower()
        if more == "n":
            break

    print(f"Saved {len(grade_list)} grade(s).")


def view_results(grade_list):
    if len(grade_list) == 0:
        print("\nNo grades yet. Choose option 1 first.")
        return

    print("\n--- Results ---")
    print("Grades  :", ", ".join(f"{g:g}" for g in grade_list))
    print(f"Average : {compute_average(grade_list):.2f}")
    print(f"Highest : {get_highest(grade_list):g}")
    print(f"Lowest  : {get_lowest(grade_list):g}")
    print(f"Status  : {get_status(grade_list)}")


def show_menu():
    print("\n===== GRADE CALCULATOR =====")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            enter_grades(grades)
        elif choice == "2":
            view_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()


# A global variable is made outside the functions, so the whole program can use it, like
# PASSING_AVERAGE and grades in my program. A local variable is made inside a function, like
# total in compute_average(), and it only works inside that function. Since total is local,
# printing it outside the function will give a NameError. I used a global for the passing grade
# since many functions need it, and I pass the grades as a parameter to keep the functions simple.