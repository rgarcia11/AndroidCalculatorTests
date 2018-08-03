import unittest
from CalculatorPageObject import CalculatorPage

class CalculatorTestPage(unittest.TestCase):

    def setUp(self):
        self.calculator_page = CalculatorPage()
    
    def test_calculator(self):
        self.calculator_page.press_number_two()
        self.calculator_page.press_number_three()

        self.calculator_page.press_number_nine()
        self.calculator_page.press_number_three()

        self.assertEqual('2393', self.calculator_page.get_result())

    def tearDown(self):
        self.calculator_page.close_app()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTestPage)
    unittest.TextTestRunner(verbosity=6).run(suite)
