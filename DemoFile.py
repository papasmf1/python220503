# DemoFile.py 
#문자열 조립(웹서버에 데이터 전송:QueryString)
url = "http://www.credu.com/?page=" + str(1)  
print(url)

import sys 

print("welcome to", "python", sep="~", end="!", file=sys.stderr)

f = open("c:/work/demo.txt", "wt")
print("file write", file=f)
f.close()

