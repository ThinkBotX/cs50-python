def area(length, width):
    return length * width


def main():
    length = int(input("Whats the length?: "))
    width = int(input("Whats the width?: "))
    room_area = area(length, width)
    print(f"The area of your room is, {room_area}ft²")


main()