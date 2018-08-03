from appium import webdriver
import unittest

class AndroidCalculatorTest(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {'automationName': 'Appium',
                                'platformName': 'Android',
                                'platformVersion': '7.1.1',
                                'deviceName': 'Android Emulator',
                                'appPackage': 'com.android.calculator2',
                                'appActivity': 'Calculator'}
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def test_sum(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual(self.driver.find_element_by_id('com.android.calculator2:id/result').text,'3')

    def test_substraction(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.assertEqual(self.driver.find_element_by_id('com.android.calculator2:id/result').text,'2')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidCalculatorTest)
    unittest.TextTestRunner(verbosity=6).run(suite)