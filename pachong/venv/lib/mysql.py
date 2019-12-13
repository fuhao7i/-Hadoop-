import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "testdb", charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 关闭数据库连接
sql1 = """CREATE TABLE COUNT (
         NAME  CHAR(40)  NOT NULL,
         COUNTRY CHAR(20)

          )"""


sql2 = """CREATE TABLE yiyuan (
         NAME  CHAR(40)  NOT NULL,
         type CHAR(20),
         degree CHAR(20)
          )"""
cursor.execute(sql2)

db.close()