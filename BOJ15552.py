import sys
x = int(input())
y = []
for i in range(x):
    a,b = map(int,sys.stdin.readline().split())
    y.append(a+b)
for l in y:
    print(l)
