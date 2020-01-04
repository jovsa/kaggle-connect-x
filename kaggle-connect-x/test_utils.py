# content of test_sample.py
import unittest
import utils


class TestMethods(unittest.TestCase):
    def test_mean_reward_happy_path(self):
        self.assertEqual(utils.mean_reward([[0, 1]]), 0.0)
        self.assertEqual(utils.mean_reward([[1, 0]]), 1.0)
