def convert(message):         # the function convert has a parameter called message which the user will input
    message = message.replace(":)", "🙂")     # Replaces :) with 🙂
    message = message.replace(":(", "🙁")     # Replaces :( with 🙁
    return message        # Here we return the modified message to be printed in the main function

def main():
    user_input = input("Please enter a message: ")     # Ask the user for input
    converted_message = convert(user_input)    # It calls the convert function with the user input and stores the result in a variable called converted_message
    print(converted_message)   # Finally, it prints the converted message to the user by


main()   # This calls the main function to execute the program