"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    How many seconds left until launch is determined in COUNTDOWN.
    """
    COUNTDOWN=10

    """Prints starting from COUNTDOWN to prevent fencepost error"""
    print(str(COUNTDOWN))

    """Count starts decreasing one at a time. This process is repeated COUNTDOWN-1 times """
    for i in range(COUNTDOWN-1):
        num=COUNTDOWN-1
        print(str(num))
        COUNTDOWN -=1

    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
