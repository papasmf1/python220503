# DemoRE.py 
#정규표현식 사용
import re 

result = re.search("[0-9]*th", "35th")
print(result)
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())


