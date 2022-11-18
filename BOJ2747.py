n = int(input())
m = 2
x = 0 
y = 1
total = 0
if n ==0:
    total = 0 
elif n == 1:
    total  = 1
    
while m <=n:
    total = x+y
    x = y
    y = total 
    m+=1

print(total)
