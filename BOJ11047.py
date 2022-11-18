import sys 
a,b = map(int,sys.stdin.readline().split())
x = []
count = 0 
for i in range(a):
    n = int(sys.stdin.readline())
    x.insert(0,n)
for k in x:
    if b%k == b:
        continue
    elif b//k !=0:
        count += b//k
        b %=k
print(count)
