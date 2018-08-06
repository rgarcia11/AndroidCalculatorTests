"""
Main test script
"""
from appium import webdriver
from CalculatorPage import CalculatorPage
import unittest

class AndroidCalculatorTest(unittest.TestCase):
    """
    Test class, run with "python -m unittest AndroidCalculatorTest"
    or "python -m unittest AndroidCalculatorTest.py".
    Running simply as "python AndroidCalculatorTest.py" also works
    as long as the following conditional (or similar) is present in the script:
        if __name__ == '__main__':
            suite = unittest.TestLoader().loadTestsFromTestCase(AndroidCalculatorTest)
            unittest.TextTestRunner(verbosity=6).run(suite)

    """
    def setUp(self):
        self.calculator_page = CalculatorPage()

    def test_sum(self):
        self.calculator_page.press_number('1')
        self.calculator_page.press_operation('add')
        self.calculator_page.press_number('2')
        self.assertEqual(self.calculator_page.get_result_text(),'3')

    def test_substraction(self):
        self.calculator_page.press_number('9')
        self.calculator_page.press_operation('sub')
        self.calculator_page.press_number('7')
        self.assertEqual(self.calculator_page.get_result_text(),'2')

    def tearDown(self):
        self.calculator_page.close_app()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidCalculatorTest)
    unittest.TextTestRunner(verbosity=6).run(suite)