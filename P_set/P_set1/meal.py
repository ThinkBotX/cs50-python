def main():
    answer = input("What time is it? ").strip()
    time = convert(answer)
    
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    # Handle and strip a.m. / p.m. suffixes if they exist
    is_pm = "p.m." in time.lower()
    time = time.lower().replace("a.m.", "").replace("p.m.", "").strip()
    
    # Split hours and minutes
    hours, minutes = time.split(":")
    hours = float(hours)
    
    # Convert 12-hour format to 24-hour float representation
    if is_pm and hours != 12.0:
        hours += 12.0
    elif not is_pm and hours == 12.0:
        hours = 0.0
        
    float_minutes = float(minutes) / 60
    return hours + float_minutes

if __name__ == "__main__":
    main()
