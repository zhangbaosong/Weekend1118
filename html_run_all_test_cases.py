#   HTMLTestRunner是基于unittest框架的一个扩展，可以自己在网上自行下载
import os
import smtplib
import unittest
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path,'rb') # 要读的内容 二进制格式
    mail_body = f.read() # 读取html报告的内容，作为邮件的正文
    f.close()

    # 要想发邮件，要把二进制的内容转成MIME格式
    # MIME mulitpurseduo 多用途 Internate 互联网 Mail 邮件 Extension 扩展
    # MIME这种格式是对邮件协议的一个扩展，使邮件不仅支持文本格式，还支持多种格式，如：图片、音频、二进制文件等

    msg = MIMEText(mail_body, 'html', 'utf-8')  # 把二进制的内容转为MIME格式

    # 上面是邮件的正文，但是对于一个邮件来讲，除了正文，还需要主题、发件人、收件人
    # msg是字典的类型，字典类似于数组，区别是：1.字典是无序的；2.

    msg['Subject'] = Header("自动化测试报告","utf-8")  # 设置邮件主题

    # 如果想用客户端软件或者自己写代码登录邮箱，很多类型的邮箱需要单独设置一个客户端授权码，这个是为了邮箱安全着想
    # 因为自己邮箱没有设置授权码，所以发件箱统一用老师的
    msg['From'] = 'bwftest126@126.com' # 设置发件箱
    # msg['To'] = '15032683126@163.com'  # 设置收件箱
    msg['To'] = '18401569214@163.com'  # 设置收件箱

    # 现在邮件内容已经准备好了，下面开始发送邮件
    # 发邮件手动步骤：
    # 1.打开登录页面，即连接邮箱服务器
    # 要想连接服务器，首先必须搞清楚网络传输协议
    # http,https,ftp,socket
    # 发邮件的协议一般有三种，要先查看一下邮箱支持哪种协议
    # 126邮箱支持这三种协议：pom3，smtp,imap
    # 我们要选一种传输协议，用来发邮件，选smtp
    # smtp simple mail transfer protocol 简单邮件传输协议
    # 首先导入smtplib的代码库
    smtp = smtplib.SMTP()   # 实例化一个SMTP类的对象
    smtp.connect("smtp.126.com")  # 连接126邮箱的服务器地址

    # 2.登录邮箱
    smtp.login("bwftest126@126.com", "abc123asd654")

    # 3.发送邮件
    # 注意：msg是MIME类型，需要转成String类型再发送
    smtp.sendmail('bwftest126@126.com', '15032683126@163.com', msg.as_string())
    smtp.sendmail('bwftest126@126.com', '18401569214@163.com', msg.as_string())
    smtp.sendmail('bwftest126@126.com', '2410064039@qq.com', msg.as_string())


    # 4.退出邮箱
    smtp.quit()
    print("email has send out!")


if __name__ == '__main__':
    # 时间戳
    # strftime: str 是String，f是format格式
    # strftime()通过这个方法可以定义时间的格式
    # Y-year年，m-month月，d-day日，H-hour小时，M-minute分，S-second秒
    now = time.strftime("%Y-%m-%d_%H-%M-%S")

    suite = unittest.defaultTestLoader.discover("./day5", pattern="*Test.py")
    # unittest.TextTestRunner() 文本测试用例运行器
    # 现在用html的测试用例运行器
    # html的测试用例运行器最终会生成一个html格式的测试报告
    # 我们至少要指定测试报告的路径
    base_path = os.path.dirname(__file__)
    print(base_path)
    path = base_path + "/report/report" + now + ".html" # 给测试报告文件名加上时间戳命名
    file = open(path, "wb")
    # stream:要创建的文件
    # title:生成的测试报告的网页标签名
    # description:描述，正文，该变量的值可以为空，为空时会默认设置正文
    HTMLTestRunner(stream=file, title="海盗商城测试报告",
                   description="测试环境:Window Server 2008 + Chrome").run(suite)
    file.close()
    # 我们要把html报告作为邮件正文，发送邮件
    send_mail(path)

    # 这时生成的测试报告，只显示类名和方法名，只能给专业的人士看
    # 我们应该把相关的手动测试用例的标题加到我们的测试报告里
    # 我们自动化测试用例是从手动测试用例中挑出来的，手工测试用例怎么
    # 写，我们就怎么编写代码，所以我们的代码里应该体现手工测试用例的标题
    # 新的测试报告会覆盖原来的测试报告，如果想把所有的测试报告保存起来要怎么做
    # 加一个时间戳，按照当前时间计算一个数字，把数字作为文件名的一部分就避免了文件名重复的问题
    # 现在我们的html格式的测试报告生成了，当测试用例全部执行完成应该生成一封提醒邮件，通知所有关心测试结果的人