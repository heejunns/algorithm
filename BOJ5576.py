x = 1
y = []
q = []
while x <=20:
    if x <=10:
        a = int(input())
        y.append(a)
        x+=1
    elif 10 <x<=20:
        b = int(input())
        q.append(b)
        x+=1
y.sort()
y.reverse()
q.sort()
q.reverse()
y1 = y[0]+y[1]+y[2]
q1 = q[0]+q[1]+q[2]
print(y1)
print(q1)


            
