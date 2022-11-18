n = int(input())
x = list(map(int,input().split()))
x.sort()
x.reverse()
y = []
n = 1
for i in x:
    y.append(i+n)
    n+=1
print(max(y)+1)
