# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

from pathlib import Path
from pprint import pprint, pformat

try: 
    # Locate Desktop
    desktop_path = Path.home() / "OneDrive" / "Escritorio"

    # Get just all the files
    files = [file for file in desktop_path.iterdir() if file.is_file()] 

    # Count file types
    file_types_counts = {}

    for file in files:
        suffix = file.suffix.lower() # e.g 'png' , 'txt'
        if suffix in file_types_counts:
            file_types_counts[suffix] += 1
        else: 
            file_types_counts[suffix] = 1

except FileNotFoundError:
    print("Error: Could not locate your Escritorio. Are you sure you are using OneDrive?")
except PermissionError:
    print("Error: You don't have permission to access some files.")
except Exception as e:
    print(f"An unexpected error ocurred: {e}")

else:
    # IT will run only if no exception was raised
    print("File type counts o your Desktop: ")
    pprint(file_types_counts)

    #Save result to a file
    output_path = Path("filecounts.txt")
    try: 
        with open(output_path, "w", encoding="utf-8") as file_out:
            file_out.write("File type counts on your Desktop:\n")
            file_out.write(pformat(file_types_counts))
        print(F"\nResults successfully saved to {output_path.resolve()}")
    except Exception as e:
        print(f"Error writing to the output file: {e}")