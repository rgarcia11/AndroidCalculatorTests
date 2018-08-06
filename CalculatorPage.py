"""
Page Object script for the calculator.
It maps buttons and interactions with the driver.
Interaction with the driver is done via
"""
from CalculatorBasePage import CalculatorBasePage


class CalculatorPage(CalculatorBasePage):
    digit = 'com.android.calculator2:id/digit_{}'
    locator_by_id = 'com.android.calculator2:id/op_{}'
    generic_prefix = 'com.android.calculator2:id/{}'

    def press_number(self, number):
        self.find_element_by_id(self.digit.format(number)).click()

    def press_operation(self, operation):
        self.find_element_by_id(self.locator_by_id.format(operation)).click()

    def press(self, button):
        self.find_element_by_id(self.generic_prefix.format(button)).click()

    def get_text(self, text_field):
        return self.find_element_by_id(self.generic_prefix.format(text_field)).text
