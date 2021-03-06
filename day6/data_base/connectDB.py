# 1.导入pymysql代码库
import pymysql

def connDb():
    # 我们要想连接数据库，需要知道数据库的哪些信息：
    # ip地址，端口号，用户名和密码，数据库名称......
    conn = pymysql.Connect(host="127.0.0.1", user="root", password="root",database="pirate", port=3306, charset='utf8')
    # 查询hd_user表中所有的数据，并且倒序打印
    sql = "select * from hd_user order by id desc"
    # 要想在代码中执行这条sql语句，首先要获取数据库的游标cursor
    curs = conn.cursor()        # 获取数据库游标
    # 通过游标执行sql语句
    curs.execute(sql)
    # 想获取数据库中最新的记录,
    # 那么就要把数据库所有记录倒序排列
    # 然后用fetchone()获取第一条记录，即数据库最新的记录
    result = curs.fetchone()
    # conn.commit()     增加、删除、修改，只需要用commit就可以了
    # 如果想获取所有的查询结果，用fetchall()
    # result = curs.fetchall()
    return result

if __name__ == '__main__':
    print(connDb())