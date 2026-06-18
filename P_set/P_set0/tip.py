def main():
    dollars = dollars_to_float(input("How much was the meal? "))         # Get meal cost from user and convert to a decimal number
    percent = percent_to_float(input("What percentage would you like to tip? "))       # Get tip percentage from user and convert to a decimal number
    tip = dollars * percent             # Calculate the tip by multiplying the meal cost by the tip percentage
    print(f"Leave ${tip:.2f}")      # Print the result to 2 decimal places


def dollars_to_float(d):
    return float(d.removeprefix('$'))       # Remove the '$' symbol and turn the string into a float


def percent_to_float(p):
    return float(p.removesuffix('%')) / 100     # Remove the '%' symbol, turn into a float, and divide by 100


main()    # Start the program