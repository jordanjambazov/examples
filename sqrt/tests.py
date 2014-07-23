import unittest
import sqrt


class SqrtTest(unittest.TestCase):
    def test_sqrt_of_four(self):
        self.assertEquals(2, round(sqrt.sqrt(4)))

    def test_sqrt_of_nine(self):
        self.assertEquals(3, round(sqrt.sqrt(9)))

    def test_sqrt_of_sixteen(self):
        self.assertEquals(4, round(sqrt.sqrt(16)))

if __name__ == '__main__':
    unittest.main()
