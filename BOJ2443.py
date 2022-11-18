n = int(input())
y = 1
x = []
z = 2
q = 0
h = 1
while y <=(2*n)-1:
    x.append("*")
    y+=1
print("".join(x))
while z <=n:
    x[q] = " "
    x[len(x)-h] = " "
    print("".join(x[:len(x)-h]))
    q+=1
    h+=1
    z+=1
