def main():
    mass = int(input("Please enter the mass of the object(in kg): "))          # Ask the user for the mass of the object and convert it to an integer
    c = 300000000              # The speed of light in meters per second
    energy = mass * c**2                   # Calculate the energy using the formula E = mc^2
    print(f"The energy of the object is {energy:,} Joules.")             # Print the energy of the object in Joules


main()                # This calls the main function to execute the program