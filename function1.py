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
print(retValue)
