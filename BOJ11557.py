n = int(input())
x = 1
q3 = [] # 최종적으로 가장 큰 대학교 
while x <=n:
    q1 = [] # 대학교 이름 
    q2 = [] # 술 먹는 양 
    x1 = 1
    n1 = int(input())
    while x1 <=n1:
        a,b = map(str,input().split())
        q1.append(a)
        q2.append(int(b))
        x1+=1
    q3.append(q1[q2.index(max(q2))])
    x+=1
for i in q3:
    print(i)
