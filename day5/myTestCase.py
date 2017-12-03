import unittest

import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        #   打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) # 此处设置时间是等待浏览器加载完成
        #   浏览器的版本和driver的版本必须匹配才能用窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(20)  # 此处设置时间是上一次测试用例执行完之后强制等待多长时间再执行下个测试用例
        self.driver.quit()