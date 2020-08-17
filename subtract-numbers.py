
"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    print("This program subtracts one number from another.")
    """Get first number from the user"""
    num1=float(input("Enter first number: "))
    """Get second number from the user"""
    num2=float(input("Enter second number: "))
    """Subtract second number from the first number"""
    num3=num1-num2
    print("The result is "+str(num3))



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
