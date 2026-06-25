import unittest

from utils.utils import suma
from utils.utils import string_reverse
from utils.utils import suma_parnyh_chisel
from utils.utils import list_string
from utils.utils import calculate_kilkist_storinok

class MyTestCasePositive(unittest.TestCase):

    def test_function_suma(self):
        result = suma(8,4)
        self.assertEqual(result, 12)

    def test_function_string_reverse(self):
        result = string_reverse('Hello world')
        self.assertEqual(result, 'dlrow olleH')

    def test_function_suma_parnyh_chisel(self):
        result = suma_parnyh_chisel(range(10))
        self.assertEqual(result, 20)

    def test_function_list_string(self):
        result = list_string(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
        self.assertIn('1', result)

    def test_function_calculate_kilkist_storinok(self):
        result = calculate_kilkist_storinok(233,8)
        self.assertEqual(result, 30)

class MyTestCaseNegative(unittest.TestCase):

    def test_function_suma_negative(self):
        result = suma(-2,-4)
        self.assertEqual(result, -6)

    def test_function_string_reverse_negative(self):
        result = string_reverse('')
        self.assertEqual(result, '')

    def test_function_suma_parnyh_chisel_negative(self):
        result = suma_parnyh_chisel([0])
        self.assertEqual(result, 0)

    def test_function_list_string_negative(self):
        result = list_string(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
        self.assertNotIn(True, result)

    def test_function_calculate_kilkist_storinok_negative(self):
        result = calculate_kilkist_storinok(0,8)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()