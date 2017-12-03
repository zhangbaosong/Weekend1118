import os
import unittest

import time
from selenium import webdriver


class DengLuTest(unittest.TestCase):
    # 3个双引号，表示文档字符串，也是一种注释，和#号 的区别就是这种种注释会显示在文档中
    """登录模块测试用例"""
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 浏览器的版本和driver的版本必须匹配才能用窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()

    def test_denglu(self):
        """登录测试正常情况测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("zhangbs")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_class_name("login_btn").click()

        #时间戳
        now = time.strftime("%Y%m%d%H%M%S")

        #   以下为截取图片断言
        base_path = os.path.dirname(__file__)
        path = base_path.replace("day5","report/image/")
        self.driver.get_screenshot_as_file(path + "denglu"+now+".png")
        print("当前用户名:zhangbs")