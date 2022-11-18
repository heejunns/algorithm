import sys
a,b,c = map(int,sys.stdin.readline().split())
total = 0 
for i in range(1,a+1):
    total += (b*i)+(c*(i**2))
print(total)

