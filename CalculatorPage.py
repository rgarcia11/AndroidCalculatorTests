"""
Page Object script for the calculator.
It maps buttons and interactions with the driver.
Interaction with the driver is done via
"""
from CalculatorBasePage import CalculatorBasePage


class CalculatorPage(CalculatorBasePage):
    others = {'decimal_separator': 'com.android.calculator2:id/dec_point',
    'delete': 'com.android.calculator2:id/del',
    'equals': 'com.android.calculator2:id/eq'}

    def press_number(self, number):
        self.find_element_by_id('com.android.calculator2:id/digit_{}'.format(number))

    def press_operation(self, operation):
        self.find_element_by_id('com.android.calculator2:id/op_{}'.format(operation)).click()

    def get_formula_text(self):
        return self.find_element_by_id('com.android.calculator2:id/{}'.format('formula')).text

    def get_result_text(self):
        return self.find_element_by_id('com.android.calculator2:id/{}'.format('result')).text