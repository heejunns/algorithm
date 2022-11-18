a,b = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
print(x[(a-1)-(b-1)])
