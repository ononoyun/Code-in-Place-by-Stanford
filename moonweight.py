"""
Write a program to prompt the user for a weight on earth
and print the equivalent weight on the moon.
"""
MOON_WEIGHT_MULTIPLIER = 0.165 #A person's weight on moon is 16.5% of his/her weight on earth
def main():
    weight_on_earth = float(input("Enter a weight on earth: "))
    print("Equivalent weight on moon: "+str(weight_on_earth*MOON_WEIGHT_MULTIPLIER))

if __name__ == '__main__':
    main()