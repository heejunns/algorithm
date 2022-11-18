import string
import sys
n = int(input()) 
x = string.ascii_uppercase
result_total = []
for i in range(n):
    y = []
    result = 0
    a = sys.stdin.readline()
    for l in x:
        if l not in a:
            y.append(l)
    for k in y:
        result+= ord(k)
    result_total.append(result)
for q in result_total:
    print(q)
