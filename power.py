# multiplication_table.py
# Program to print multiplication table of a number
import sys

def multiplication_table(num):
    """Function to return multiplication table as a list"""
    return [num * i for i in range(1, 11)]

if __name__ == "__main__":
    print("\n---- Multiplication Table ----\n")
    try:
        # Case 1: Argument passed (CLI)
        if len(sys.argv) == 2:
            num = int(sys.argv[1])
        # Case 2: No arguments passed (user input)
        else:
            num = int(input("Enter a number: "))

        table = multiplication_table(num)

        for i, value in enumerate(table, start=1):
            print(f"{num} x {i} = {value}")

    except ValueError:
        print("Invalid input! Please enter an integer.")
