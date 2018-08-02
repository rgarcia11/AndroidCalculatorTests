from appium import webdriver
from BasePageObject import BasePage

class CalculatorPage(BasePage):

    number_two = "com.android.calculator2:id/digit_2"
    number_three = "com.android.calculator2:id/digit_3"
    number_nine = "com.android.calculator2:id/digit_9"
    addition_character = "com.android.calculator2:id/op_add"
    result = "com.android.calculator2:id/result"

    def press_number_two(self):
        web_element2 = self.find_element_by_id(self.number_two)
        web_element2.click()

    def press_number_three(self):
        web_element3 = self.find_element_by_id(self.number_three)
        web_element3.click()

    def press_addition(self):
        web_element_add = self.find_element_by_id(self.addition_character)
        web_element_add.click()

    def press_number_nine(self):
        web_element9 = self.find_element_by_id(self.number_nine)
        web_element9.click()

    def get_result(self):
        return self.find_element_by_id(self.result).text