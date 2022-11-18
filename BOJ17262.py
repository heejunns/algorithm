n = int(input())
x = []
y = []
m1 = 1
m2 = 0
count = 0
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
for l in range(len(x)-1):
    if x[m1] > y[m2]:
        count+=1
    m1+=1
if count!= 0 :
    print((max(x)-min(y)))
else:
    print(0)


