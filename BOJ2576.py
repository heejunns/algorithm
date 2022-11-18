n = 7 
x = 0 
y = []
z = []
while x < 7:
    a = int(input())
    y.append(a)
    x+=1

for i in y:
    if i%2 != 0:
        z.append(i)

if z == []:
    print(-1)
else:
    print(sum(z))
    print(min(z))
