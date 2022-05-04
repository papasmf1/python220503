# DemoFile2.py 

#파일에 쓰기(r: raw string notation)
f = open(r"c:\work\test.txt", "wt", encoding="utf-8")
f.write("첫줄에\n두번째는\n마지막\n")
f.close() 

