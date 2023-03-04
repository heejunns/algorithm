# 백준 1158번, 요세푸스 문제
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split()) # n, k 를 입력 받기
total  = deque([i for i in range(1,n+1)]) # 1 부터 n 까지의 요소를 가지도록 생성
result = [] # 나온 사랃들을 저장 할 리스트
count = k-1 # 몇번째 사람을 꺼내야 하는지 카운트 하기 위한 변수
while len(total) > 0: # 모두 꺼낼때가지 반복
    if count > 0: # count 가 0 보다 크다면 꺼냈다가 다시 추가하기
        l = total.popleft()
        total.append(l)
        count-=1
    elif count == 0: # count 가 0 이면 꺼내기
        result.append(total.popleft()) # 꺼낸 사람 result 리스트에 저장
        count = k-1
print("<" , end = "")
for i in range(len(result)):
    if i == len(result)-1:
        print(str(result[i])+">")
    else:
        print(str(result[i])+", ", end = "")