def calculate_area(length, width):
    """Calculates the area of a rectangle in square feet."""
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


def get_choice(prompt, options):
    """Ensures the user selects a valid option from a list."""
    while True:
        value = input(prompt).strip().lower()
        if value in options:
            return value
        print(f"Invalid choice. Please choose from: {', '.join(options)}")


def main():
    print("------ Ultimate Bangladeshi Property & Cost Calculator ------")
    
    # Conversion Constants
    SQFT_PER_KATHA = 720.0
    SQFT_PER_DECIMAL = 435.6
    
    # Nested data structure to organize everything
    # Format: {category_name: {"area": float, "type": "indoor"/"outdoor", "cost_rate": float}}
    property_data = {}
    
    while True:
        category = input("\nEnter area name (e.g., Ghor, Uthan, Pukur) or type 'done': ").strip().capitalize()
        
        if category.lower() == 'done':
            if not property_data:
                print("No data entered.")
                return
            break
            
        if not category:
            print("Name cannot be blank.")
            continue
            
        # 1. Check Indoor vs Outdoor
        space_type = get_choice(f"Is {category} 'indoor' or 'outdoor'? ", ['indoor', 'outdoor'])
        
        # 2. Check Addition vs Subtraction
        action = get_choice(f"Do you want to 'add' this area or 'subtract' it from totals? ", ['add', 'subtract'])
        
        # 3. Get Dimensions
        print(f"--- Dimensions for {category} ---")
        length = get_positive_float("Length (ft): ")
        width = get_positive_float("Width (ft): ")
        calculated_area = calculate_area(length, width)
        
        # Apply negative sign if it is a subtraction area
        if action == 'subtract':
            calculated_area = -calculated_area
            
        # 4. Cost Estimation Setup
        price_rate = get_positive_float(f"Enter estimated cost rate per sq ft for {category} (৳): ")
        
        # Save data
        if category in property_data:
            property_data[category]['area'] += calculated_area
        else:
            property_data[category] = {
                "area": calculated_area,
                "type": space_type,
                "cost_rate": price_rate
            }
            
        print(f"Recorded: {category} ({space_type.upper()}) = {calculated_area:,.2f} sq ft at ৳{price_rate:,.2f}/sq ft")

    # --- FINAL REPORT GENERATION ---
    print("\n================================================================================================")
    print("                                     FINAL PROPERTY REPORT                                      ")
    print("================================================================================================")
    
    total_indoor_area = 0
    total_outdoor_area = 0
    total_cost = 0
    
    for name, data in property_data.items():
        area = data['area']
        space_type = data['type']
        rate = data['cost_rate']
        
        # Calculate cost based on absolute area (even subtracted spaces cost money to build)
        item_cost = abs(area) * rate
        total_cost += item_cost
        
        # Track indoor vs outdoor totals
        if space_type == 'indoor':
            total_indoor_area += area
        else:
            total_outdoor_area += area
            
        # Local conversions
        area_katha = area / SQFT_PER_KATHA
        area_decimal = area / SQFT_PER_DECIMAL
            
        # Format printing based on addition vs subtraction
        status = "(Subtracted)" if area < 0 else ""
        
        # FIXED format string order: :>alignment,commas.precisionf
        print(f"* {name:<12} | {space_type.upper():<7} | {area:>11,.2f} sq ft | {area_katha:>9,.2f} Katha | {area_decimal:>9,.2f} Dec {status:<12} | Cost: ৳{item_cost:>14,.2f}")

    net_total_area = total_indoor_area + total_outdoor_area
    
    net_katha = net_total_area / SQFT_PER_KATHA
    net_decimal = net_total_area / SQFT_PER_DECIMAL
    indoor_katha = total_indoor_area / SQFT_PER_KATHA
    outdoor_katha = total_outdoor_area / SQFT_PER_KATHA

    print("------------------------------------------------------------------------------------------------")
    print(f"Total Indoor Area:  {total_indoor_area:>11,.2f} sq ft  ({indoor_katha:,.2f} Katha)")
    print(f"Total Outdoor Area: {total_outdoor_area:>11,.2f} sq ft  ({outdoor_katha:,.2f} Katha)")
    print(f"NET PROPERTY AREA:  {net_total_area:>11,.2f} sq ft  ({net_katha:,.2f} Katha / {net_decimal:,.2f} Decimal)")
    print("------------------------------------------------------------------------------------------------")
    print(f"TOTAL ESTIMATED PROPERTY COST: ৳{total_cost:,.2f}")
    print("================================================================================================")


if __name__ == "__main__":
    main()
