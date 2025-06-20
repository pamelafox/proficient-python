import unittest

from sum_scores import sum_scores

class TestSumScores(unittest.TestCase):

    def test_sum_empty(self):
        self.assertEqual(sum_scores([]), 0)

    def test_sum_numbers(self):
        self.assertEqual(sum_scores([8, 9, 7]), 24)

if __name__ == '__main__':
    unittest.main()