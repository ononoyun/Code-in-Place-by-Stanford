"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random


def main():
    """
    This program prints random integers (with values between 0 and 100, inclusive).
    NUM_RANDOM determines the number of random numbers to print.
    Minimal and maximal values of the random numbers generated are specified in MIN_RANDOM and MAX_RANDOM.
    """
    NUM_RANDOM=10
    MIN_RANDOM=0
    MAX_RANDOM=100

    """repeats the generation and printing of random numbers NUM_RANDOM times"""
    for i in range(NUM_RANDOM):
        num1=random.randint(MIN_RANDOM,MAX_RANDOM)
        print(str(num1))



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
