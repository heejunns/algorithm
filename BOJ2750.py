t = int(input())
x = 1
y = []
while x<=t:
    a = int(input())
    y.append(a)
    x+=1
y.sort()
for i in y:
    print(i)
