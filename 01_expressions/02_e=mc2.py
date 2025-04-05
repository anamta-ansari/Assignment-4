# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

def main():
    mass  : float = float(input("Enter the mass of the object in kg: "))
    C : int = 299792458 
    e  = mass * C **2

    # Display work to the user
    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(C) + " m/s")

    print(f"{e} joules of energy")

if __name__ == '__main__':
    main()