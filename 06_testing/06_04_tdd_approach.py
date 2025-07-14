# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

from unittest import TestCase
from pathlib import Path

def add(n):
    sum = n + 10
    return sum

def subtract(n):
    result = 10 - n
    return result

def create_file():
    file =  open("test_io.txt", "w")
    file.close()

def read_file():
    with open("test_io.txt", "r") as file:
       content = file.read()
    return content

def write_file():
    with open("test_io.txt", "w") as file:
        content = file.write("Bye!")
        return content

read_file()


class TestIO(TestCase):

    # add numbers with n + 10
    def test_add_result(self):
        self.assertEqual(add(2),12)

    # subtract numbers
    def test_subtract_result(self):
        self.assertEqual(subtract(2),8)

    #check if test_io.txt file exists
    def test_if_file_exists(self):
        message = "No doesn't exists."
        file_path = Path("test_io.txt")
        self.assertEqual(file_path.is_file(), True, message)

    #check if test_io.txt file can be read
    def test_if_can_read_file(self):
        message = "No can't read."
        """Instead of checking the exact string how to check readability in general?"""
        self.assertEqual(read_file(), "Bye!", message)
           

    #check if test_io.txt file can be written
    def test_if_can_write_file(self):
        message = "No can't write."
        self.assertEqual(write_file(), 4, message)