x = 1
y = []
z = []
q = []
while x <= 3:
    a,b = map(int,input().split())
    y.append(a)
    z.append(b)
    x+=1
if y.count(y[0]) == 1:
    q.append(y[0])
elif y.count(y[0]) == 2:
    if y[0] == y[1]:
        q.append(y[2])
    elif y[0] == y[2]:
        q.append(y[1])
if z.count(z[0]) == 1:
    q.append(z[0])
elif z.count(z[0]) == 2:
    if z[0] == z[1]:
        q.append(z[2])
    elif z[0] == z[2]:
        q.append(z[1])
print(q[0],q[1])
