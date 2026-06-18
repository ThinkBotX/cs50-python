def main():
    x = int(input("Whats x?: "))
    if parity(x):
        print("Even")
    else:
        print("Odd")
    

def parity(n):
    return n % 2 == 0


main()