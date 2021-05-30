import unittest
import leapyear

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz.fizz_buzz(100),100)

if __name__ == '__main__': 
    unittest.main(verbosity=2) 
