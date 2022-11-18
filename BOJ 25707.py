import sys
n = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
x.sort()
x.reverse()
total = 0 
for i in range(n-1):
    total += (x[i]-x[i+1])
total+=(x[0]-x[len(x)-1])
print(total)



