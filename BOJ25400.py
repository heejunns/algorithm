n = int(input())
x = list(map(int,input().split()))
y = 1
q = []
for i in x:
    if i == y:
        q.append(i)
        y+=1
print(n-len(q))
