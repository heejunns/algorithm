n = 10 
x = 1
y = []
z = 0

while x <= n :
    a,b = map(int,input().split())
    if x == 1:
        q = b-a
        y.append(q)
        x+=1
    else:
        q = (y[z]+(b-a))
        y.append(q)
        z+=1
        x+=1

print(max(y))
