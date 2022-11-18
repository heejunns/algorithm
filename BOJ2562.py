x = 1
y =[]
while x <=9:
    a = int(input())
    y.append(a)
    x+=1
print(max(y))
print(y.index(max(y))+1)

