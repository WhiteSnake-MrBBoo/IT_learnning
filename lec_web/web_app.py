from bs4 import BeautifulSoup
import requests

url = "https://star.ytn.co.kr/news/list.php?mcd=0117&hcd=04"
res = requests.get(url)
html_doc = res.text
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    a = add(4,3)
    print(a)

    b = ytn_craw()

    c = {"x":["Mar 1", "Mar 2", "Mar 3"],"y" :[10000, 30162, 26263]}

    d={"x":["January", "February", "March", "April"], "y":[4215, 5312, 6251, 7841]}

    return render_template("index.html"
                           , MY_ADD=a
                           , MY_YTN_LIST=b
                           , MY_CHART_DICT=c
                           , MY_BAR_CHART_DICT=d)



def ytn_craw() :
    mylist=[]
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
        mylist.append(   {"title":title, "rdate":rdate, "img":img, "href":href}   )

    #print(mylist)
    return mylist

def add(num1, num2):
        res = num1 + num2
        return res

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777, debug=True)

