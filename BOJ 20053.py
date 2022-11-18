# 최소,최대 2
n = int(input())
result = []
for i in range(n):
    a = int(input())
    x = list(map(int,input().split()))
    result.append([min(x),max(x)])
for k in result:
    print(k[0],k[1])
