n = int(input())
x = list(map(int,input().split()))
x.sort()
total = 0 
y = []
for i in x:
    total+=i
    y.append(total)
print(sum(y))
