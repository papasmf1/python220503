# function1.py 
#함수를 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("함수내부:", x)

#호출
retValue = setValue(5)
print(retValue)

#리턴하는 경우
def swap(x,y):
    return y,x 

#호출
retValue = swap(3,4)
print(retValue[0])
print(retValue[1])

#가변형(참조형식)과 불변형(값형식) 
a = 1.2
print(id(a))
a = 2.3
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#문자의 교집합을 리턴 
def intersect(prelist, postlist):
    #교집합 글자를 담을 지역변수(List)
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print(intersect("HAM","SPAM"))
