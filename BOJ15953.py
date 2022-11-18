t = int(input())
x = 1
y = []
z = []
while x <= t:
    a,b = map(int,input().split())
    if 21>=a >=1:
        if a == 1:
            y.append(5000000)
        elif 2 <=a<=3:
            y.append(3000000)
        elif 4<=a<=6:
            y.append(2000000)
        elif 7<=a<=10:
            y.append(500000)
        elif 11<=a<=15:
            y.append(300000)
        elif 16<=a<=21:
            y.append(100000)
    else:
        y.append(0)
    if 31>=b>=1:
        if b == 1:
            y.append(5120000)
        elif 2<=b<=3:
            y.append(2560000)
        elif 4<=b<=7:
            y.append(1280000)
        elif 8<=b<=15:
            y.append(640000)
        elif 16<=b<=31:
            y.append(320000)
    else:
        y.append(0)
    z.append(y[0]+y[1])
    y.clear()
    x+=1
for i in z:
    print(i)
