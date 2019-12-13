import pymysql

import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot
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
#print(res1)
#print(res2)
#print(res3)
x0 = []
y0 = []
for raw in res1:
            zhi = raw
            x0.append(zhi[0])
            y0.append(zhi[1])


trace_basic = [go.Bar(
      # x=['惊奇队长','头号玩家','何以为家','杀人者','见龙卸甲','一个母亲的复仇','流浪地球','上海风云之夺宝金龙','鬼吹灯之巫峡棺山','雪暴','非常人贩','小猪佩奇过大年','巅峰营救','西虹市首富','龙猫'
       #   ,'飞驰人生','风语咒','悲伤逆流成河'],
      # y=['']
      x=x0,y=y0,
    )]
# Layout
layout_basic = go.Layout(
            title = '电影热度分析',
            xaxis = go.XAxis(range = [-0.5,30.5], domain = [0,1])
    )
# Figure
figure_basic = go.Figure(data = trace_basic, layout = layout_basic)
# Plot
pyplt(figure_basic, filename='2.html')


db.close()