#   有了myTestCase以后，再写测试用例时，就不需要重新写setUP 和 tearDown 方法了
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    # 3个双引号，表示文档字符串，也是一种注释，和#号 的区别就是这种种注释会显示在文档中
    """注册模块测试用例"""
    #   因为myTestCase已经实现了 setUp 和 tearDown 方法，我们以后再写测试用例就不需要重新实现setUp 和 tearDown方法
    def test_zhu_ce(self):
        """打开注册页面的测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg") # 获取注册页面路径
        # driver.current_url   #  用来获取当前浏览器中的网址
        actual = driver.title   # 用来获取当前浏览器中的标签页的title
        # 标题式断言
        expected = "用户注册 - 道e坊商城 - Powered by Haidao111"
        self.assertEqual(actual, expected)
        # 截取图片式断言
        #  get_screenshot_as_file 截取整个浏览器的图片
        base_path = os.path.dirname(__file__)   # 创建相对路径
        path = base_path.replace("day5","report/image/")
        # 如果报错提示浏览器版本是62. ...  ，那么卸载浏览器重新安装
        driver.get_screenshot_as_file(path + "zhuce.png")
