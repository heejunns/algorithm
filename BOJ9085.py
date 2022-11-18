n = int(input()) # 테스트 개수 
x =1 
z = 0
q = []
while x <= n:
    m = int(input()) # 자연수의 개수 
    y = list(map(int,input().split())) # 자연수의 개수 만큼의 자연수 
    for i in y:
        z+=i
    q.append(z)
    z = 0 
    x+=1

for i in q:
  print(i) # 하나씩 출력 
