a,b = map(int,input().split())
x = []
n = int(input())
for i in range(n):
    q = int(input())
    x.append(abs(q-b))
if abs(b-a) >= min(x)+1:
    print(min(x)+1)
elif abs(b-a) < min(x)+1:
    print(abs(b-a))