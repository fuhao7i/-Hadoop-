import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "wangyuyan", charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

res1 = []
res2 = []
res3 = []

sql1 = """
            select * from dianying

          """
sql2 = """
            select * from dianshiju

          """
sql3 = """
            select * from zongyi
          """
cursor.execute("""select * from dianying""")
results = cursor.fetchall()
for row in results:
    zhi = row
    res1.append(zhi)
cursor.execute(sql2)
results = cursor.fetchall()
for row in results:
    zhi = row
    res2.append(zhi)
cursor.execute(sql3)
results = cursor.fetchall()
for row in results:
    zhi = row
    res3.append(zhi)
print(res1)
print(res2)
print(res3)

db.close()