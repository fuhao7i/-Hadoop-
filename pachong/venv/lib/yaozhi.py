import requests
import re
import pymysql

def main():
    cookies = "think_language=zh-CN; kztoken=nJail6zJp6iXaJqWl29kYWRxYZib; his=a%3A2%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl29kYWRxYZeU%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl29kYWRxYZib%22%3B%7D; _gat=1; MEIQIA_EXTRA_TRACK_ID=1NUcJTyLkJtGba7Zl9gVl45DnQb; expire=1562156326185; ypxs_show=true; _ga=GA1.3.1760558625.1562139044; MEIQIA_VISIT_ID=1NUcJTZyblUf2pyxxmXgCW2MuUW"
    print(type(cookies))
    cook_lst = cookies.split(";")
    cook_dict = {}
    print(type(cook_lst))
    print(cook_lst)
    for i in cook_lst:
        kv = i.strip()
        kv_lst = kv.split("=")
        k = kv_lst[0]
        v = kv_lst[1]
        cook_dict[k] = v
    print(cook_dict)
    base_url = "https://db.yaozh.com/jinkou?p="
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    rets = []
    lst = []

    db = pymysql.connect("127.0.0.1", "root", "123456", "testdb")
    cursor = db.cursor()
    """insert_stmt = (
        "INSERT INTO count(name,country)"
        "VALUES (%s, %s)"
    )"""
   # sql = """INSERT INTO count
   #          VALUES (%s,%s)"""

    for i in range(10):
        j = i+1
        url = base_url + str(j)
        resp = requests.get(url, headers=header, cookies=cook_dict)
        #print(resp)
        #print(resp.status_code)
        data = resp.content.decode("utf-8")
        #print(data)
        with open("1.html", "w") as f:
            f.write(data)

        pattern0 = re.compile("""target="_blank">([\u4e00-\u9fa5]*)</a></td>""")
        pattern1 = re.compile("""<td>([\u4e00-\u9fa5]*)</td>""")
        ret0 = pattern0.findall(data)
        ret1 = pattern1.findall(data)
        #ret = pattern1.findall(data)
        for q in range(0,10):
            y = ret0[q]

            z = ret1[q]

            x = (y,z)

            #print(x)
            lst.append(x)

    base_url1 = "https://db.yaozh.com/hmap?p="

    sql1 = """INSERT INTO yiyuan
               VALUES (%s,%s,%s)"""

    rets = []
    lst1 = []
    for h in range(10):
        j = h+1
        url1 = base_url1 + str(j)
        resp1 = requests.get(url1, headers=header, cookies=cook_dict)
        #print(resp)
        #print(resp.status_code)
        data1 = resp1.content.decode("utf-8")
        #print(data)
        with open("2.html", "w") as f:
            f.write(data1)

        pattern3 = re.compile("""target="_blank">([\u4e00-\u9fa5]*)</a></th>""")
        pattern4 = re.compile("""等</td>			                	            <td>([\u4e00-\u9fa5]*)</td>""")
        pattern5 = re.compile("""医院</a></th>
              			                	            <td>([\u4e00-\u9fa5]*)</td>""")
        ret3 = pattern3.findall(data1)
        ret4 = pattern4.findall(data1)
        ret5 = pattern5.findall(data1)
        print(ret5)
        #ret = pattern1.findall(data)
        for q in range(0,10):
            y = ret3[q]

            z = ret4[q]

            f = ret5[q]

            x = (y,z,f)

            print(x)
            lst1.append(x)
    for w in lst1:
         try:
               cursor.execute(sql1,w)
               db.commit()
         except:
               print("insert error")
               db.rollback()



    #db.close()
    print(lst)
    #print(lst1)



if __name__ == "__main__":
    main()
