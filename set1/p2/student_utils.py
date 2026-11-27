"""
Name: KENJIMOR CELESTINO
Section: IV-BSIT B
Activity: P2 - Custom Module: student_utils
"""

# passing grade is 75, since that is the usual passing mark
PASSING_GRADE = 75


def calculate_average(grades):
    # add all the grades and divide by how many grades there are
    return sum(grades) / len(grades)


def determine_pass_fail(average):
    # if the average is 75 and above, the student passed
    if average >= PASSING_GRADE:
        return "Passed"
    return "Failed"


def get_highest(grades):
    # max() gets the biggest number in the list
    return max(grades)


def get_lowest(grades):
    # min() gets the smallest number in the list
    return min(grades)


# this only runs when we open this file directly,
# since it will not run when another file imports it
if __name__ == "__main__":
    sample = [85, 90, 78, 92, 70]
    avg = calculate_average(sample)

    print("Testing student_utils.py")
    print("Average:", avg)
    print("Result:", determine_pass_fail(avg))
    print("Highest:", get_highest(sample))
    print("Lowest:", get_lowest(sample))