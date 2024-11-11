#HW 8
import unittest
from src.homework.i_dictionaries_and_sets import add_inventory # type: ignore
from src.homework.i_dictionaries_and_sets import remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        widgets = {}
        expected_widget = {'Widget1':10}
        self.assertEqual(expected_widget, add_inventory (widgets, 'Widget1', 10))
        quantity=widgets.get('Widget1')

        expected_widget = {'Widget1':35}
        self.assertEqual(expected_widget, add_inventory (widgets, 'Widget1', quantity+25))
        quantity=widgets.get('Widget1')

        expected_widget = {'Widget1':25}
        self.assertEqual(expected_widget, add_inventory (widgets, 'Widget1', quantity-10))

    def test_remove_inventory_widget(self):
        widgets = {'Widget1':12 , 'Widget2':4}
        remove_inventory_widget(widgets, 'Widget1')
        expected_widgets = {'Widget2':4}
        self.assertEqual(1, widgets.len())
        self.assertEqual(expected_widgets, widgets)
