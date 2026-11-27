"""
Name: KENJIMOR CELESTINO
Section: IV-BSIT B
Activity: P2 - Custom Module: student_utils
"""

print("-jjjk")
#python3 set1/p2/p2_main.py

# import style 1: import the whole module, and we use student_utils.function()
import student_utils

# import style 2: import only the functions we need, and we use them directly
from student_utils import get_highest, get_lowest

# built-in module, since we need the current date and time for the report
from datetime import datetime


def read_grades():
    # ask how many grades, and keep asking until the input is valid
    while True:
        try:
            count = int(input("How many grades will you enter? "))
            if count > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    grades = []

    # ask for each grade, and only accept 0 to 100
    for i in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {i}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


def main():
    print("=== Student Grade Report ===")
    grades = read_grades()

    # using import style 1 (module name first)
    average = student_utils.calculate_average(grades)
    status = student_utils.determine_pass_fail(average)

    # using import style 2 (no module name needed)
    highest = get_highest(grades)
    lowest = get_lowest(grades)

    # datetime shows when the report was made
    generated = datetime.now().strftime("%B %d, %Y %I:%M %p")

    print("\n--- Report ---")
    print(f"Grades entered : {grades}")
    print(f"Average        : {average:.2f}")
    print(f"Highest grade  : {highest}")
    print(f"Lowest grade   : {lowest}")
    print(f"Result         : {status}")
    print(f"Report generated on: {generated}")


# run main() only when this file is the one being executed
if __name__ == "__main__":
    main()
