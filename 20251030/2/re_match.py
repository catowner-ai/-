# match(regex, string)
# search(regex, string)

import re

result1 = re.match("a*b","abb aab abbbb abc")    #只抓符合的第一筆
print(result1.group())
print(result1)



print(re.findall(r"a*b","abb aab abbbb abc"))  #抓符合的所有資料



