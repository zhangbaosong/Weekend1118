import unittest

import time

from day5.myTestCase import MyTestCase
from day6.data_base.connectDB import connDb


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("zhangbs1203")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        driver.find_element_by_name("mobile_phone").send_keys("13651240136")
        driver.find_element_by_name("email").send_keys("13651240136@163.com")
        driver.find_element_by_class_name("reg_btn").click()
        # 检查数据库中新增的记录的用户名和我们输入的用户名是否一致
        expected = "zhangbs1203"
        time.sleep(3)
        actual = connDb()[1]
        self.assertEqual(expected, actual)
        print(expected)
        print(connDb()[1])