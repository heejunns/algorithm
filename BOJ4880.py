mport sys
x = []
n = 0 
m = 1
while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a== 0 and b == 0 and c ==0:
        break
    if a != 0 and b != 0 and c != 0 :
        if b/a == c/b:
            x.append("GP")
            x.append(int(c*(b/a)))
        elif (b-a) == (c-b):
            x.append("AP")
            x.append(c+(b-a))
    else:
        x.append("AP")
        x.append(c+(b-a))
for i in range(len(x)//2):
    print(x[n],x[m])
    n+=2
    m+=2
