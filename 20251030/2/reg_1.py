# findall(regex, string)
import re

regex = ".?lccnet[0-9]*"
test_string="lccnet is good lccnet yayaya lccnet127 not bad"

result=re.findall(regex,test_string)
print(type(result))
print(result)
print(result[0])
print(result[1])
print(result[2])



