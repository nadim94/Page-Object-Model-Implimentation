import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
import time

sys.path.append("D:/PageObjectModel")
# Note: page file import after sys path
# Cmd command: python testCase/LoginTest.py

from pageObject.LoginPage import LoginPage


class loginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/login"
    userName = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="D:\PageObjectModel\drivers\chromedriver_win32\chromedriver.exe")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.userName)
        lp.setPassword(self.password)
        lp.click_login()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Title Not Match")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/PageObjectModel/reports'))

