import unittest
import fizzbuzz

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz.fizz_buzz(98),98)

    def test_2(self):
        self.assertEqual(fizzbuzz.fizz_buzz(9),"fizz")

    def test_3(self):
        self.assertEqual(fizzbuzz.fizz_buzz(25),"buzz") 

if __name__ == '__main__': 
    unittest.main(verbosity=2) 
