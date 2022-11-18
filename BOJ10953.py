n = int(input())
x = 1
y = []
while x<=n:
    a = input()
    y.append(int(a[0])+int(a[2]))
    x+=1
for i in y:
    print(i)
