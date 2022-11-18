a,b = map(int,input().split())
x = 1
y = []
while x<=a:
    if a%x == 0:
        y.append(x)
        x+=1
    else:
        x+=1
if len(y) < b:
    print(0)
else:
    print(y[b-1])
