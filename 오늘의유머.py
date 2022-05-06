# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식 사용 
import re 

#웹봇(웹로봇)
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        #<td class="subject">
        # <a href="/board/view.php">아이 셋 키우는 아빠의 육아팁</a>
        # </td>
        #특정 태그의 속성들(attrs)
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        tag = item.find("a")
                        title = tag.text
                        print(title.strip())
                        # if (re.search('애플', title)):
                        #         print(title.strip())
                except:
                        pass
        
