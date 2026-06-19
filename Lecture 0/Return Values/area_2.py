# A single, reusable function for any rectangular area
def calculate_area(length, width):
    return length * width


def main():
    # House calculations
    house_length = int(input("House length?: "))
    house_width = int(input("House width?: "))
    house_total = calculate_area(house_length, house_width)
    print(f"The area of your House is {house_total}ft²")

    # Yard calculations
    yard_length = int(input("Yard length?: "))
    yard_width = int(input("Yard width?: "))
    yard_total = calculate_area(yard_length, yard_width)
    print(f"The area of your Yard is {yard_total}ft²")

    # Total calculations
    total_area = house_total + yard_total
    print(f"So, the total area of both your house and yard is {total_area}ft²")


main()
