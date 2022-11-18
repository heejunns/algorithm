a,b = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
for i in x:
    if i <=b:
        b+=1
    else:
        break
print(b)

