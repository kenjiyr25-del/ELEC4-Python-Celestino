"""
P4: Safe Menu Program
Name: Kenjimor Celestino
Section: IV-BSIT B
Topics: Exceptions (try, except, else, finally)
"""
print("-jjjk")
#python3 set1/p4/p4_exceptions.py

def divide_numbers():
    """Ask for two numbers and divide them, handling bad input."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Invalid number. Please enter digits only (e.g., 10 or 3.5).")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    else:
        # Runs only when no exception happened
        print(f"Result: {num1} / {num2} = {result}")
    finally:
        # Always runs, error or not
        print("Division operation finished.")


def open_file():
    """Ask for a file name and display its contents."""
    filename = input("Enter the file name (e.g., sample.txt): ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    else:
        print(f"\n--- Contents of {filename} ---")
        print(contents if contents else "(The file is empty.)")
        print("--- End of file ---")
    finally:
        print("File operation finished.")


def show_menu():
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Divide two numbers")
    print("2. Open a file")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(f"Invalid choice '{choice}'. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()