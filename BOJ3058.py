t = int(input()) # 테스트 개수 
x = 1
total = 0 
z = []
q = []
while x<=t:
    number = list(map(int,input().split()))
    for i in number:
        if (i%2) == 0 :
            z.append(i)
    for l in z:
        total+=l
    q.append(total) # 짝수 합 
    q.append(min(z)) # 짝수들중에 최소 값
    total = 0 
    z.clear()
    x+=1

x = 1
q1 = 0 
q2 = 1
while x<=t:
    print(q[q1],q[q2])
    q1+=2
    q2+=2
    x+=1

            
