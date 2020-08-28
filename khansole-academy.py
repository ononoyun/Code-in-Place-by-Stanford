"""
File: khansole_academy.py
-------------------------
This program tests addition skill.
If user answers three correct in a row, user passes the test!
"""

import random

MIN_NUMBER = 10
MAX_NUMBER = 99
# Number of correct answers in a row is denoted by N
N = 3

def main():

    #When user gets an answer correct, variable 'correct' is incremented by 1.
    #When 'correct' equals N, the program will stop with a message "Congratulations! You mastered addition."

    correct = 0
    while correct != N:
        n1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        n2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        n3 = n1 + n2
        print("What is " + str(n1) + "+" + str(n2) + "?")
        answer = int(input("Your answer: "))
        if answer == n3:
            correct += 1
            print("Correct! You've gotten " + str(correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(n3))

    if correct == N:
        print("Congratulations! You mastered addition.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

