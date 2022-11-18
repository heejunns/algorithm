x = []
y = []
q = []
n = 1
for i in range(8):
    a = int(input())
    x.append(a)
    y.append(a)
x.sort()
for i in y:
    if x[3]<=i:
        q.append(n)
    n+=1
print(sum(x[3:]))
for i in q:
    print(i,end=" ")
