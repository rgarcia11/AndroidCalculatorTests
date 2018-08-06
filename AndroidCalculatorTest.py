"""
Main test script
"""
import unittest

from CalculatorPage import CalculatorPage


class AndroidCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator_page = CalculatorPage()

    def test_sum(self):
        self.calculator_page.press_number('1')
        self.calculator_page.press_operation('add')
        self.calculator_page.press_number('2')
        self.assertEqual(self.calculator_page.get_text('result'), '3')

    def test_substraction(self):
        self.calculator_page.press_number('9')
        self.calculator_page.press_operation('sub')
        self.calculator_page.press_number('7')
        self.assertEqual(self.calculator_page.get_text('result'), '2')

    def tearDown(self):
        self.calculator_page.close_app()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidCalculatorTest)
    unittest.TextTestRunner(verbosity=6).run(suite)
