# BOJ 아이 러브 크로아티아 
import sys
time = 0 
k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
x = []
y = []
for i in range(n):
    a,b = map(str,sys.stdin.readline().strip().split())
    x.append([int(a),b])
for l in x:
    if l[1] == "T":
        if int(l[0])+time >= 210:
            break
        k+=1
        time+=int(l[0])
    elif l[1] == "N" or l[1] == "P":
        if int(l[0])+time >= 210:
           break
        time+=int(l[0])
if k%8 == 0:
    print(k)
else:
    print(k%8)

