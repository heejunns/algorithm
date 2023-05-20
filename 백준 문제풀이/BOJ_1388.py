# 백준 1388번 바닥 장식
import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
tai = [] 
for i in range(n):
    input = list(sys.stdin.readline().strip())
    tai.append(input)
count = 0
for i in range(n):
    s = 0
    for l in range(m):
        if tai[i][l] == "-" and s == 0:
            s = 1
            count+=1
        elif tai[i][l] == "|":
            s = 0
for i in range(m):
    s = 0
    for l in range(n):
        if tai[l][i] == "|" and s == 0:
            s = 1
            count+=1
        elif tai[l][i] == "-":
            s = 0
print(count)

            
    

