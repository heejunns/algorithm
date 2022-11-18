# BOJ 11024 더하기 4
n = int(input())
y = []
for _ in range(n):
    x = list(map(int,input().split()))
    y.append(sum(x))
for i in y:
    print(i)

