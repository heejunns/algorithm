n,m = map(int,input().split()) # 첫 줄에 입력 받는 N,M
x = 1
y = []
h = []
while x<=m:
    a,b = map(int,input().split())
    y.append(a) # b는 비교할 필요가 없기 때문에 a만 이용
    x+=1
x = 1 # x를 다시 1로 초기화 아래 최소 비용 찾을 때 다시 이용 
count = 0 
for i in y:
    if i >=n:
        count+=1 # 일단 a가 N과 같거나 큰 수를 걸러내서 경품을 받을 수 있는 포인트 카드 우선적으로 걸러내기 
    else:
        h.append(i) # a 가 부족한 애들 다른 도장으로 바꿔야 함 
if (m-1) == count: # 이미 M-1 을 채웠다면 0을 출력하고 종료 
    print(0)
else:
    z = []
    for l in h:
        z.append(n-l) # 각각의 a들이 얼마나 늘어나야 경품을 받을 수 있는지 만들기 
    z.sort() # 최소 비용이니까 가장 작은 비용부터 정리 
    total = 0 
    for k in z:
        if x<=((m-1)-count): # 모자란 경품 가능 포인트 카드 만큼 최소비용 사용
            total+=k
            x+=1
        else:
            break
    print(total)
