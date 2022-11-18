n = int(input())
x = 1
count = 0
y = []
z = 1
while x <= n:
    a = input()
    for i in a:
        if i =="O":
            count+=z
            z+=1
        elif i =="X":
            count+=0
            z=1
    y.append(count)
    z = 1
    count = 0 
    x+=1
for l in y:
    print(l)
