# DemoRE.py 
#정규표현식 사용
import re 

result = re.search("[0-9]*th", " 35th")
print(result)
# result = re.match("[0-9]*th", " 35th")
# print(result)
# print(result.group())
#문자열 패턴
print(bool(re.search("ap", "this is apple")))
print(bool(re.search("\d{4}", "올해는 2022년입니다.")))
print(bool(re.search("\d{5}", "우리동네는 52300입니다.")))

result = re.search("\d{5}", "우리동네는 52300입니다.")
print(result.group())




