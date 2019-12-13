import requests
import re


def main():
    url = "https://3w.huanqiu.com/a/34f321/7NYDI8H4hUs?agt=8"
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    resp = requests.get(url, headers=header)
    data = resp.content.decode("utf-8")

    pattern = re.compile("""<p>(.*)</p>""")
    ret = pattern.findall(data)
    print(ret)


if __name__ == "__main__":
    main()