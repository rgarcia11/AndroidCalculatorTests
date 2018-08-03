from appium import webdriver

class CalculatorBasePage:
    def __init__(self):
        desired_capabilities = {'automationName': 'Appium',
                                'platformName': 'Android',
                                'platformVersion': '7.1.1',
                                'deviceName': 'Android Emulator',
                                'appPackage': 'com.android.calculator2',
                                'appActivity': 'Calculator'}
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def find_element_by_id(self, locator):
        return self.driver.find_element_by_id(locator)

    def close_app(self):
        self.driver.quit()