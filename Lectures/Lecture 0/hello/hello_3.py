# 1) Ask user for their name + remove whitespace from str and capitalise user's name
name = input("Whats your name?: ").strip().title()

# 2) Split user's name into first name and last name
first, last = name.split(" ")

# 3) Say hello to the user:
print(f"Hello, {last}")