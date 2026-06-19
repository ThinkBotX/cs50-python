def main():
    x = int(input("Whats x?: "))
    print(f"x squared is {square(x)}")


def square(n):
    return pow(n, 2)


main()