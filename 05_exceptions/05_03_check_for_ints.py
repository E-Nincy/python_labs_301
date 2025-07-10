# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.


while True:
    user_input = input("Please enter an integer: ")

    try: 
        number = int(user_input)
        print(f"Thank you! You entered the integer: {number}")
        break

    except ValueError:
        print("Oops! That's not an integer. Please try again.")
