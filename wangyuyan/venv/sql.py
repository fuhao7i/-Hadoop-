import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "wangyuyan", charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 关闭数据库连接
sql1 = """CREATE TABLE dianying (
         NAME  CHAR(40)  NOT NULL,
         redu CHAR(20)

          )"""

sql2 = """CREATE TABLE dianshiju (
         NAME  CHAR(40)  NOT NULL,
         redu CHAR(20)

          )"""

sql3 = """CREATE TABLE zongyi (
         NAME  CHAR(40)  NOT NULL,
         redu CHAR(20)

          )"""

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)


db.close()