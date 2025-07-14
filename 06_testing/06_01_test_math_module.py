# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import math
from unittest import TestCase

class TestMath(TestCase):

    def test_fmod_remainder(self):
        self.assertEqual(math.fmod(5,2),1)

    def test_sqrt_result(self):
        self.assertEqual(math.sqrt(9),3)

    def test_prod_elements(self):
        sequence = (1,2,3)
        self.assertGreater(math.prod(sequence), 5)