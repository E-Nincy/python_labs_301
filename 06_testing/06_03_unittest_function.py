# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)


from unittest import TestCase

def addition(num):
    sum = num + num
    return sum

class sumTest(TestCase):

    def test_addition(self):
        self.assertEqual(addition(2),4)

    def test_addition_false(self):
        self.assertFalse(addition(2),4)