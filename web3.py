# web2.py 
#웹서버에 페이지 실행 요청
import urllib.request
#크롤링 
from bs4 import BeautifulSoup


#페이지 번호 생성
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")

    for tag in cartoons:
        title = tag.find("a")
        print(title.text.strip())