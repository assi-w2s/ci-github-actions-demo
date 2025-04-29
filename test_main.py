import unittest
from main import compute_mean

class TestSumFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(compute_mean([2, 4, 6, 8]), 5.0)

if __name__ == '__main__':
    unittest.main()
