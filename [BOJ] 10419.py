import sys
n= int(sys.stdin.readline())
m = 0 
q = []
for i in range(n):
    x = int(sys.stdin.readline())
    while True:
        if m+(m**2) == x:
            q.append(m)
            m = 0 
            break
        elif m+(m**2) > x:
            q.append(m-1)
            m =0 
            break
        m+=1
for i in q:
    print(i)