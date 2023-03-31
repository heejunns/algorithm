# 백준 2217번, 로프
import sys
n = int(sys.stdin.readline()) # 정수 n 입력받기, 로프의 개수
ropes = [] # 입력받은 로프의 정보를 저장할 리스트
for i in range(1,n+1):
    rope = int(sys.stdin.readline()) # 각각의 로프의 최대 중량 정보 입력 받기
    ropes.append(rope)

total = 0
max_kg = 0
ropes.sort(reverse=True) # 오름차순으로 정렬
for j in range(0,len(ropes)): # 로프가 버틸 수 있는 최대 중량의 크기가 큰 로프 부터 꺼내서 병렬 연결을 했을 때 가장 큰 무게를 버틸 수 있는 무게를 찾기 
    total =  ropes[j]*(j+1)
    if max_kg < total: # 저장되어 있는 최대 버틸 수 있는 무게보다 크다면 최대 버틸 수 있는 무게 변경
        max_kg = total
print(max_kg)



