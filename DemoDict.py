# DemoDict.py 
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device)
#입력
device["맥북"] = 15 
print(device)
#수정
device["아이폰"] = 6 
print(device)

#삭제
del device["아이폰"]
#검색
print(device["아이패드"])

#중단점(Break Point)
for item in device.items():
    print(item)

#명함관리
phone = {"kim":"1111", "lee":"2222"}
print(phone)
print("kim" in phone)
print("kang" not in phone)

#복사본을 생성
p = phone 
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone), id(p))

#얕은복사
a = [1,2,3]
b = a
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

#깊은복사(Deep Copy)
print("---깊은 복사---")
a = [1,2,3]
b = a[:]
a[0] = 100
print(a)
print(b)
print(id(a), id(b))

import copy 
a = [100,200,300]
b = copy.deepcopy(a)
a[0] = 101 
print(a)
print(b)

print(bool(1 < 2))
print(bool(1 != 2))
print(bool(1 == 2))
print(5/2)
print(5//2)
print(5%2)
