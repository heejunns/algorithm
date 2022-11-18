x = int(input())
z = []
for i in range(x):
    y = list(map(int,input().split()))
    z.append(min(y))
for l in z:
    print(l)
