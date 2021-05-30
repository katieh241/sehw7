import unittest
import fizzbuzz

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz.fizz_buzz(100),100)

    def test_2(self):
        self.assertEqual(fizzbuzz.fizz_buzz(9),"fizz")

if __name__ == '__main__': 
    unittest.main(verbosity=2) 
