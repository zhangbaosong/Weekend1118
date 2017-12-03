import time
from selenium import webdriver
from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage


class RegTest(MyTestCase):
    def test_reg(self):
        lp = LoginPage(self.driver)
        lp.open()
        # time.sleep(3)
        lp.click_reg_button()
