#HW 7

import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value
from src.homework.g_lists_and_tuples.lists import get_highest_list_value
class Test_Config(unittest.TestCase):

    def test_get_lowest_list_value(self):
        self.assertEqual(1, get_lowest_list_value([8,10,1,50,20]))

    def test_get_highest_list_value(self):
        self.assertEqual(50, get_highest_list_value([8,10,1,50,20]))