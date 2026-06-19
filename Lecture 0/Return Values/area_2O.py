def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width


def get_positive_float(prompt):
    """Safely gets a positive decimal number from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("--- Dynamic Property Area Calculator ---")
    
    # Dictionary to store the name of the area and its calculated size
    areas = {}
    
    while True:
        # 1. Ask for the category name
        category = input("\nEnter area category (e.g., House, Yard, Pool, Garage) or type 'done' to finish: ").strip().capitalize()
        
        # Check if the user is finished entering areas
        if category.lower() == 'done':
            if not areas:
                print("No areas were entered.")
                return
            break
            
        if not category:
            print("Category name cannot be blank.")
            continue
            
        # 2. Get dimensions for this specific category
        print(f"--- Entering dimensions for: {category} ---")
        length = get_positive_float(f"Enter {category} length (ft): ")
        width = get_positive_float(f"Enter {category} width (ft): ")
        
        # 3. Calculate and store the area
        calculated_area = calculate_area(length, width)
        
        # If the category already exists, add to it; otherwise, create a new entry
        if category in areas:
            areas[category] += calculated_area
        else:
            areas[category] = calculated_area
            
        print(f"Added: {category} area = {calculated_area:,.2f}ft²")

    # 4. Print individual and total results
    print("\n==================================")
    print("         FINAL AREA REPORT        ")
    print("==================================")
    
    total_area = 0
    for category, area in areas.items():
        print(f"* {category}: {area:,.2f}ft²")
        total_area += area
        
    print("----------------------------------")
    print(f"TOTAL PROPERTY AREA: {total_area:,.2f}ft²")
    print("==================================")


if __name__ == "__main__":
    main()
