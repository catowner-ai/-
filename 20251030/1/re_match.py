# match(regex, string)
# search(regex, string)

import re

result1 = re.match("a*b","abb aab abbbb abc")   
print(result1.group())



