import math

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

def pythagoras():
    AB = int(input("Enter the length of AB: "))
    AC = int(input("Enter the length of AC: "))
    BC = int(math.sqrt(AB ** 2 + AC ** 2)  )
    print("The length of BC is:", BC)

if __name__ == "__main__":
    pythagoras()  
