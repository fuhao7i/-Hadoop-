import requests
import re
import pymysql

def main():
    #cookies = "think_language=zh-CN; kztoken=nJail6zJp6iXaJqWl29kYWRxYZib; his=a%3A2%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl29kYWRxYZeU%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl29kYWRxYZib%22%3B%7D; _gat=1; MEIQIA_EXTRA_TRACK_ID=1NUcJTyLkJtGba7Zl9gVl45DnQb; expire=1562156326185; ypxs_show=true; _ga=GA1.3.1760558625.1562139044; MEIQIA_VISIT_ID=1NUcJTZyblUf2pyxxmXgCW2MuUW"
    #print(type(cookies))
    #cook_lst = cookies.split(";")
    #cook_dict = {}
    #print(type(cook_lst))
   # print(cook_lst)
    #for i in cook_lst:
       # kv = i.strip()
       # kv_lst = kv.split("=")
       # k = kv_lst[0]
       # v = kv_lst[1]
       # cook_dict[k] = v
    #print(cook_dict)
    db = pymysql.connect("127.0.0.1", "root", "123456", "wangyuyan", charset='utf8')
    cursor = db.cursor()
    sql1 = """INSERT INTO dianying
                 VALUES (%s,%s)"""
    sql2 = """INSERT INTO dianshiju
                    VALUES (%s,%s)"""
    sql3 = """INSERT INTO zongyi
                    VALUES (%s,%s)"""

    url = "http://top.iqiyi.com/dianying.html"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    rets = []
    lst = []




    resp = requests.get(url, headers=header)
        #print(resp)
        #print(resp.status_code)
    data = resp.content.decode("utf-8")
        #print(data)
    with open("1.html", "w") as f:
        f.write(data)

    pattern0 = re.compile("""title="([\u4e00-\u9fa5]*)" target="_blank" data-aid=""")
    pattern1 = re.compile("""<em><i class="icon-fyb-hot"></i>热度&nbsp;(.*)</em>""")
    ret0 = pattern0.findall(data)
    ret1 = pattern1.findall(data)
        #ret = pattern1.findall(data)
    #print (ret0)
    #print(ret1)

    e=0
    for q in range(0,30):

            y = ret0[e]
            e=e+2
            z = ret1[q]

            x = (y,z)

            #print(x)
            lst.append(x)
    for w in lst:
        try:
            cursor.execute(sql1,w)
            db.commit()
        except:
            print("insert error")
            db.rollback()

    print(lst)

    url1 = "http://top.iqiyi.com/dianshiju.html"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    rets = []
    lst1 = []




    resp = requests.get(url1, headers=header)
        #print(resp)
        #print(resp.status_code)
    data = resp.content.decode("utf-8")
        #print(data)
    with open("2.html", "w") as f:
        f.write(data)

    pattern0 = re.compile("""title="([\u4e00-\u9fa5]*)" target="_blank" data-aid=""")
    pattern1 = re.compile("""<em><i class="icon-fyb-hot"></i>热度&nbsp;(.*)</em>""")
    ret2 = pattern0.findall(data)
    ret3 = pattern1.findall(data)
        #ret = pattern1.findall(data)
    #print (ret0)
    #print(ret1)

    e=0
    for q in range(0,33):

            y = ret2[e]
            e=e+2
            z = ret3[q]

            x = (y,z)

            #print(x)
            lst1.append(x)
    for w in lst1:
        try:
            cursor.execute(sql2, w)
            db.commit()
        except:
            print("insert error")
            db.rollback()

    print(lst1)



    url2 = "http://top.iqiyi.com/zongyi.html"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    rets = []
    lst2 = []




    resp = requests.get(url2, headers=header)
        #print(resp)
        #print(resp.status_code)
    data = resp.content.decode("utf-8")
        #print(data)
    with open("3.html", "w") as f:
        f.write(data)

    pattern0 = re.compile("""title="([\u4e00-\u9fa5].*)" target="_blank" data-aid=""")
    pattern1 = re.compile("""<em><i class="icon-fyb-hot"></i>热度&nbsp;(.*)</em>""")
    ret4 = pattern0.findall(data)
    ret5 = pattern1.findall(data)
        #ret = pattern1.findall(data)
    #print (ret0)
    #print(ret1)

    e=0
    for q in range(0,40):

            y = ret4[e]
            e=e+2
            z = ret5[q]

            x = (y,z)

            #print(x)
            lst2.append(x)
    for w in lst2:
        try:
            cursor.execute(sql3, w)
            db.commit()
        except:
            print("insert error")
            db.rollback()

    print(lst2)


if __name__ == "__main__":
    main()