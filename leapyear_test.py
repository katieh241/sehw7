import unittest
import leapyear

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(leapyear.isleapyear(a),0)

if __name__ == '__main__': 
    unittest.main(verbosity=2) 
