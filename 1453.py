n = int(input())
x = list(map(int,input().split()))
count = 0 
print(list(range(1,n+1)))
for i in x:
    if i in y:
        y.pop(y.index(i))  
print(len(y)) 
