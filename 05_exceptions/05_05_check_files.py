# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

from pathlib import Path

file_path = Path("C:/Users/escot/OneDrive/Escritorio/Codingnomads/python-301-main/05_exceptions/integers.txt")

try: 
    with open(file_path, "r", encoding="utf-8") as file:
        first_line = file.readline().strip()
        number = int(first_line) # it may raise ValueError
except IOError:
    print(f"Error: could not read file '{file_path}'. Check if the file exists and is accessible.")
except ValueError:
    print(f"Error: The first line in '{file_path}' is not a valid integer.")
else:
    # will run only if no exception was raised
    result = number * 2
    print(f"The number is: {number}")
    print(f"the result of multiplying it by 2 is. {result}")