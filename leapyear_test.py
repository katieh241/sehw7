import unittest
import leapyear

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(leapyear.isleapyear("a"),0)

    def test_2(self):
        self.assertEqual(leapyear.isleapyear(2004),"true")

    def test_3(self):
        self.assertEqual(leapyear.isleapyear(1900), "false")

    def test_4(self):
        self.assertEqual(leapyear.isleapyear(2400), "true")

    def test_5(self):
        self.assertEqual(leapyear.isleapyear(2077), "false")

if __name__ == '__main__': 
    unittest.main(verbosity=2) 
