# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

try:
    numerator = float(input("Enter the numerator: "))
    demoninator = float(input("Enter the denominator: "))

    quotient = numerator / demoninator
    print(f"The quotient is: {quotient}")

except ValueError:
    print("Error: Please enter valid numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")