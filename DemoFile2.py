# DemoFile2.py 

#파일에 쓰기(r: raw string notation)
#로우 푸드(가공하지 않은 음식): 통밀빵, 현미... 
f = open(r"c:\work\test.txt", "wt", encoding="utf-8")
f.write("첫줄에\n두번째는\n마지막\n")
f.close() 

#파일 읽기
f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
#처음으로 이동
print(f.tell())
f.seek(0)
#약간의 보정
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
#처음으로 이동
f.seek(0)
lst = f.readlines() 
print(lst)
for item in lst:
    print(item)

f.close() 
