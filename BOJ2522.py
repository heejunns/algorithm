n = int(input())
x = 1
y = []
z = 1
while x <=n:
    y.append(" ")
    x+=1
x -=1
n -= (n-1)
while x >=n:
    y[len(y)-z] = "*"
    print("".join(y))
    z+=1
    x-=1
x +=2
z-=1
while x <=z:
    y[len(y)-z] = " "
    print("".join(y))
    z-=1

