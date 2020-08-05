"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():

    #Get input from the user.
    n = int(input("n: "))

    #Input should be a positive integer.
    while n<=0:
        n = int(input("n: "))

    #Number of steps to reach n=1 will be stored and incremented in variable "p"
    p = 0

    while n != 1:
        if n%2 == 0 :
            print(str(n)+" is even, so I take half: "+str(int(n/2)))
            n = int(n/2)
            p += 1

        else:
            print(str(n) + " is odd, so I make 3n+1: " + str(int(3*n+1)))
            n = int(3*n+1)
            p += 1

    print("The process took "+str(p)+" steps to reach 1")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
