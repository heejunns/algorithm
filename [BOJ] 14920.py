import sys 
n = int(sys.stdin.readline())
x = []
for i in range(20):
    if n%2 == 0:
        n = (n%2)
        x.append(n)
    elif n%2 == 1:
        n  = ((n*3)+1)
        x.append(n)
print(x)