# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

from pathlib import Path

# Define the path to the 'books' folder
books_dir = Path(__file__).resolve().parent / "books"

# -------- Read war_and_peace.txt --------
try:
    with open(books_dir / "war_and_peace.txt", "r", encoding="utf-8") as f:
        war_and_peace_text = f.read()
        print("[✓] war_and_peace.txt read successfully.")
except Exception as e:
    print(f"[✗] Failed to read war_and_peace.txt: {e}")
    war_and_peace_text = None  # So we can still continue later

# -------- Overwrite crime_and_punishment.txt with an empty string --------
try:
    with open(books_dir / "crime_and_punishment.txt", "w", encoding="utf-8") as f:
        f.write("")  # Overwrite file with nothing
        print("[✓] crime_and_punishment.txt cleared.")
except Exception as e:
    print(f"[✗] Failed to overwrite crime_and_punishment.txt: {e}")

# -------- Print the first character from each file --------
book_files = [
    "war_and_peace.txt",
    "pride_and_prejudice.txt",
    "crime_and_punishment.txt"
]

print("\n--- First characters from each file ---")
for book in book_files:
    file_path = books_dir / book
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            first_char = f.read(1)
            if first_char:
                print(f"{book}: '{first_char}'")
            else:
                print(f"{book}: [EMPTY FILE]")
    except FileNotFoundError:
        print(f"{book}: File not found.")
    except IOError as e:
        print(f"{book}: Could not read the file. Reason: {e}")
