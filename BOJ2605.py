import sys
n = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
y = [1]
n = 2
for i in x[1:]:
    y.insert(len(y)-i,n)
    n+=1
for l in y:
    print(l,end = " ")
