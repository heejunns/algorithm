# 백준 14235번, 크리스마스 선물
import sys
n = int(sys.stdin.readline()) # 아이들과 거점지를 방문한 횟수 n 을 입력받기
santa_ = [] # 산타가 가지고 있는 선물을 저장할 리스트
result = [] # 아이들에게 준 선물의 가치를 저장할 리스트
for i in range(n):
    input_a = list(map(int, sys.stdin.readline().rstrip().split())) # a 입력받기
    if len(input_a) == 1: # 입력받은 a 의 길이가 1 이라면 0 을 입력했다는것을 알 수 있다. 
        if len(santa_) == 0: # 산타가 가지고 있는 선물이 없다면
            result.append(-1)
        else: # 산타의 선물 중 가치가 가장 높은 선물을 주기
            result.append(santa_.pop())
    else: # a 의 길이가 1이 아니라면 선물을 충전할 거점이라는 뜻 이니까 
        santa_.extend(input_a[1:]) # 선물들 저장
        santa_.sort() # 오름차순으로 선물을 정리
for j in result:
    print(j)

