n = int(input())
problems = list(map(int,input().split()))
count = 1 
total = 0 
for i in problems:
    if i == 1:
        total += count 
        count+=1
    else:
        count = 1
    
print(total)
