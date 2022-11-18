n = int(input())
y = 1
x = []
z = 1
q = 0
h = 1
while y <=(2*n)-1:
    x.append("*")
    y+=1

while z <=n:
    if z ==1:
        print("".join(x))
        z+=1
    else:
        x[q] = " "
        x[len(x)-h] = " "
        print("".join(x[:(len(x)-h)]))
        q+=1
        h+=1
        z+=1
z-=2
n -= (n-1)
q-=1
h-=1
while z>=n:
    x[q] = "*"
    x[len(x)-h] ="*"
    q-=1
    h-=1
    print("".join(x[:len(x)-h]))
    z-=1                      
