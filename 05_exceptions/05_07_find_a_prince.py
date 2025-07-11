# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

# Custom exception
class PrinceException(Exception):
    def __init__(self, message="The word 'Prince' was found in content. "):
        super().__init__(message)

# Read .txt files from 'books'
import os

books_folder = ("C:/Users/escot/OneDrive/Escritorio/Codingnomads/python-301-main/05_exceptions/books")


try: 
    for filename in os.listdir(books_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(books_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read(100) 
            if "Prince" in content:
                raise PrinceException(f"'Prince' was found in the first 100 characters of {filename}")
            else:
                print(f"{filename}: No 'Prince' found in the first 100 characters.")
except PrinceException as e:
    print(f"Custom exception raised! : {e}")
except Exception as general_error:
    print(f"Something went wrong: {general_error}")