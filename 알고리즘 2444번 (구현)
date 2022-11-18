n = int(input())
y = 1
x = []
z = 1
q = 1
while y <=(2*n)-1:
    x.append(" ")
    y+=1

while z <=n:
    if z ==1:
        x[len(x)//2] = "*"
        print("".join(x[:((len(x)//2)+1)]))
        z+=1
    elif z <=n:
        x[(len(x)//2)-q] = "*"
        x[(len(x)//2)+q] = "*"
        q+=1
        print("".join(x[:((len(x)//2)+q)]))
        z+=1
z-=2
n -= (n-1)
q-=1
while z>=n:
    x[(len(x)//2)-q] = " "
    x[(len(x)//2)+q] = " "
    print("".join(x[:(len(x)//2)+q]))
    q-=1
    z-=1                      
    
