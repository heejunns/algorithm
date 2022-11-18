a,b,c = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = list(map(int,input().split()))
x.sort()
y.sort()
z.sort()
x.reverse()
y.reverse()
z.reverse()
result = []
result1 = sum(x)+sum(y)+sum(z)
result.append(result1)
result2 = 0 
while True:
    result2+=(int((x[0]+y[0]+z[0])*0.9))
    x.pop(0)
    y.pop(0)
    z.pop(0)
    if x == [] or y == [] or z == []:
        break
if x != []:
    result2+=sum(x)
if y != []:
    result2+=sum(y)
if z != []:
    result2+=sum(z)
result.append(result2)
print(result[0])
print(result[1])


