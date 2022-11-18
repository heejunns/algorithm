# BOJ 23881 알고리즘 수업 - 선택 정렬 1
# 해결 아이디어는 그냥 선택 정렬을 수행할때 입력된 k 교환 횟수 일때 교환 되는 원소 두개를 출력 하고 만약 k 번째 전에 선택 정렬이 끝난다면 -1을 출력한다. 
'''n,k = map(int,input().split())
x = list(map(int,input().split()))
count = 0 # 교환 횟수 
m = 0 # 비교하는 시작 범위를 제어할때, 비교 후 교환 할 때 위치 사용  
for  _ in range(len(x)-1): # 반복문 비교 횟수는 원소의 길이 만큼 반복 , 가장 큰 값은 가장 오른쪽 끝에 있기 때문에 마지막 비교는 할 이유가 없음 따라서 리스트 길이에서 -1 해주기 
    min = x[m] 
    for i in x[m+1:]: # 비교 시작 위치 부터 for문으로 가장 작은 값 찾기 , 이미 min에 비교 범위의 시작인 x[m]이 저장되어 있기 때문에 m+1 원소부터 비교하면 됨 
        if min > i:
            min = i
    if x[m] != min: # 가장 작은 값을 찾을때 x[m] 과 min 값이 다르다면 작은 값을 찾은 거니까 x[m] 자리와 가장 작은값을 교환 하기 같다면 교환할 이유가 없음. x[m]이 가장 작은 값이기 때문에 
        count+=1 # 교환 횟수를 하나씩 올리기 
        if count == k: # count 와 k의 값이 같다면 출력하고 for 문을 빠져 나간다. 
            if x[m] > min: 
                print(min,x[m])
                break
            else:
                print(x[m],min)
                break
        tmp = x[m] # 교환 하는 과정 
        x[x.index(min)] = tmp
        x[m] = min
    m+=1 # 비교 범위를 조절하는 m 하나씩 증가 
if count < k:# count의 값이 k보다 작다면 -1을 출력 
    print(-1)
'''

n,k = map(int,input().split())
x = list(map(int,input().split()))
count = 0 
m = len(x)-1 
for _  in range(len(x)-1):
    max = x[m]
    for i in x[:m]:
        if max < i :
            max = i
    if max != x[m]:
        count+=1
        if count == k :
            if x[m] > max:
                print(max,x[m])
                break
            else:
                print(x[m],max)
                break
        tmp = x[m]
        x[x.index(max)] = tmp
        x[m] = max
    m-=1
if count < k:
    print(-1)




