# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

try:
    number = 10
    result = number / 0
    print(f"The resultis: {result}")

except ZeroDivisionError as e:
    print("Oops! You can't divide by zero")
    print(f"Error details {e}")