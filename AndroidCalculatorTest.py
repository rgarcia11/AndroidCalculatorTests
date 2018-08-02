import unittest


class AndroidCalculatorTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '7.1.1', 'deviceName': 'Android Emulator'}