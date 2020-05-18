# 1 Finding using simple way
# 2 Greedy Matching With Regex

import re

x = 'From: Using the : character Fro: me also'
m = re.findall('^From: Using*',x) #Start from F and till the end where there is :
print(m)

n = re.findall('^Fro\S+:',x) #Start from F and inclue until you get whitespace
print(n)

y = re.findall('^F.+:',x) 
# '^' means F should be at beginning '.' means any character '+' means followed by 
# any character one or more until you found the last ':' symbol (LAST SYMBOL)
print(y)