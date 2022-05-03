# class2.py 
#1) 클래스를 정의
class Person:
    #클래스 멤버 변수(데이터 공유)
    num_person = 0 
    #초기화 메서드
    def __init__(self):
        #자기 멤버변수를 초기화
        self.name = "default name"
        Person.num_person += 1 
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#2) 인스턴스(복사본)생성
p1 = Person() 
p2 = Person() 
p3 = Person() 
print("인스턴스 개수:", Person.num_person)

#런타임시에 변수추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)


