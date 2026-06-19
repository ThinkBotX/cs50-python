# 1) Ask user for their name
name = input("Whats your name?: ") 

# Remove whitespace from str and capitalise user's name
name = name.strip().title()

# 2) Say hello to the user:
# Method - 1
print("Hello, ", end="")
print(name +"!")

# Method - 2
print("Hello, " + name + "!")

# Method - 3
print("Hello,",name,"!")

# Method - 4
print(f"Hello, {name}!")