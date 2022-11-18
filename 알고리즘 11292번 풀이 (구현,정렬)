q = []
while True:
    x = []
    y = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        a,b = map(str,input().split())
        if x == []:
            x.append(a)
            y.append(float(b))
        elif y[0] < float(b):
            x.clear()
            y.clear()
            x.append(a)
            y.append(float(b))
        elif y[0] == float(b):
            x.append(a)
            y.append(float(b))
    q.append(x)
for l in q:
        if len(l) == 1:
            print(l[0])
        elif len(l) >1:
            for k in l:
                print(k,end = " ")
            

