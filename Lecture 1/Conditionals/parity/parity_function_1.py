def main():
    x = int(input("Whats x?: "))
    if parity(x):
        print("Even")
    else:
        print("Odd")
    

def parity(n):
    if n % 2 == 0:
        return True
    else:
        return False 

main()