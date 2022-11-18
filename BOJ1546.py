n = int(input())
x = list(map(int,input().split()))
y = []
for i in x:
    y.append((i*100)/max(x))
print(sum(y)/n)
