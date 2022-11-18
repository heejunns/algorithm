import sys
n = int(sys.stdin.readline())
result = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if x<=y:
        result.append(y)
if result == []:
    print(-1)
else:
    print(min(result))