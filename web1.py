# web1.py 
from bs4 import BeautifulSoup

#페이지 로딩
#메서드나 함수를 연속해서 호출: 메서드 체인 
page = open("c:\\work\\test01.html", 
    "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<p> 몽땅 검색
#print(soup.find_all("p"))
#<a> 전부 
#print(soup.find_all("a"))
#필터링: <p class=outer-text>:파이썬 키워드(class)충돌
#print(soup.find_all("p", class_="outer-text"))

#내부 문자열만 리턴
for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)


