# DemoStr.py 
#print(dir(str))

#문자열 생성
names = ["홍길동","전우치","이순신"]
for name in names:
    print("안녕하세요 {0}님! 이제는 더운 여름입니다.".format(name))
    print("=" * 40)

#문자열 처리
u = "<<< spam and ham >>>"
result = u.strip("<> ")
print(u)
print(result)
strA = "python is very poweful"
print(len(strA))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p",7))
result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print("---다시 원복---")
print(":)".join(lst))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("MBC2580".isdecimal())
print("2580".isdecimal())
print(strA.endswith("ful"))
print(strA.startswith("python"))

