n = int(input())
x = 1
q = []
while x <= n:
    y = list(map(int,input().split()))
    y.sort()
    if (y[3]-y[1]) >=4:
        q.append("KIN")
        x+=1
    else:
        q.append(y[1]+y[2]+y[3])
        x+=1
for i in q:
    print(i)
