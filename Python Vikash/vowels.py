# find all vowels between two consonent from string
import re

findall = re.finditer(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])', input())
fill = list(map((lambda x: x.group()), findall))
if len(fill) == 0:
    print(-1)
else:
    for s in fill:
        print(s)