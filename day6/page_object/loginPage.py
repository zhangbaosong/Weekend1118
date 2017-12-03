from selenium.webdriver.common.by import By

# 登录页面类
class LoginPage:
    # 构造方法的作用
    # 实例化LoginPage对象的时候，必须要调用构造方法，
    # python中构造方法是固定写法，用__init__表示  构造方法
    # 需要把driver作为参数传进来
    # 便于别的属性和方法使用driver
    def __init__(self, driver):
        self.driver = driver

    # 页面标题
    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    # 页面网址
    url = "http://localhost/index.php?m=user&c=public&a=login"

    # 小括号表示元组，元组中有两个元素，第一个元素是控件的定位方式
    # 第二个元素是控件定位方式的具体值
    username_input_loc = (By.ID, "username")    # 获取用户名元素位置
    password_input_loc = (By.ID, "password")    # 获取密码元素位置
    login_button_loc = (By.CLASS_NAME, "login_btn")     # 获取登录按钮元素位置
    reg_button_loc = (By.CLASS_NAME, "reg")


    # 打开网页方法
    def open(self):
        self.driver.get(self.url)

    # 输入用户名方法
    def input_username(self, username):
        # self.driver.find_element_by_id("username").send_keys(username)
        # self.driver.find_element(By.ID, "username").send_keys(username)
        # *号的作用就是把一个元组中的元素分别传入方法参数中
        # 前面加一个星号，表示传入的就不是元组了，而是元组中的两元素
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    # 输入密码方法
    def input_password(self, password):
        # self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    # 点击登录按钮方法
    def click_login_button(self):
        # self.driver.find_element_by_class_name("login_btn").click()
        self.driver.find_element(*self.login_button_loc).click()

    # 点击立即注册按钮方法
    def click_reg_button(self):
        self.driver.find_element(*self.reg_button_loc).click()