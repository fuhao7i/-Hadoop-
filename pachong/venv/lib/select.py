import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "testdb", charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

res = []
sql1 = """
            select * from count

          """
sql2 = """
            select * from yiyuan

          """
cursor.execute(sql2)
results = cursor.fetchall()
for row in results:
    zhi = row
    res.append(zhi)
print(res)


db.close()