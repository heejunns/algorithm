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
        print("".join(x[:(len(x)//2)+1]))
        z+=1
    else:
        x[(len(x)//2)-q] = "*"
        x[(len(x)//2)+q] = "*"
        q+=1
        z+=1
        print("".join(x[:(len(x)//2)+q]))
