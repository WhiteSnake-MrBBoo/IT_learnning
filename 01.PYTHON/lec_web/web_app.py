from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    a = add(4,3)
    print(a)

    b = ytn_craw()

    c = {"x": ["Mar 1", "Mar 2", "Mar 3"], "y":[10000, 30162, 26263] }

    d = {"x": ["January", "February", "March", "April"], "y":[4215, 5312, 6251, 7841] }
    return render_template("index.html"
                           , MY_ADD=a
                           , MY_YTN_LIST=b
                           , MY_CHART_DICT=c
                           , MY_BAR_CHART_DICT=d
                           )


def ytn_craw() :
    mylist = []
    url = "https://star.ytn.co.kr/news/list.php?mcd=0117&hcd=04"
    res = requests.get(url)
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    news_list = soup.select("#container > div > div.content > div > div.news_list_wrap > div")
    for news in news_list:
        title = news.select_one("div.text_area > div.title > a").text
        rdate = news.select_one("div.text_area > div.info > div.date").text
        img = news.select_one("div.photo > a > img").get("data-src")
        href = news.select_one("div.text_area > div.title > a").get("href")
        #print(title, rdate, img, href)
        mylist.append(  {"title":title, "rdate":rdate, "img":img, "href":href}  )

    # print(mylist)
    # [{'title': '아이들 소연, 5년 2개월 만에 솔로 컴백…9월 초 출격', 'rdate': '2026.08.19. 13:09',
    #   'img': 'https://image.ytn.co.kr/general/jpg/2026/0819/202608191309270831_h.jpg',
    #   'href': 'https://star.ytn.co.kr/_sn/0117_202608191309270831'},
    #  {'title': '로이킴, 임영웅·이찬원·추영우 이어 김종국까지…작사·작곡가로 영역 확장', 'rdate': '2026.08.19. 11:12',
    #   'img': 'https://image.ytn.co.kr/general/jpg/2026/0819/202608191112438733_h.jpg',
    #   'href': 'https://star.ytn.co.kr/_sn/0117_202608191112438733'},
    #  ]
    return mylist


def add(num1, num2):
        res = num1 + num2
        return res

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777, debug=True)