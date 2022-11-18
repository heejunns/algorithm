import sys
n = int(input())
x = [1,2,3]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    x1 = x.index(b)
    x2 = x.index(a)
    x[x1] = a
    x[x2] = b
print(x[0])
