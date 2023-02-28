# 백준 2161번, 카드1
import sys
from collections import deque
n = int(sys.stdin.readline()) # 정수 n 입력 받기
cards = deque([i for i in range(1,n+1)]) # 1 부터 입력 받은 n 까지 각각의 요소를 리스트로 생성 후 deque 로 감싸기
result = [] # 버린 카드를 저장 할 리스트
count = 0 # 카드를 버리거나 카드를 뽑아 카드 아래로 내리거나를 값으로 구분 할 변수
# 카드의 순서는 0번 인덱스가 가장 위에 있는 카드로 기준을 정함
while len(cards) > 1: # cards 의 카드 개수가 하나 남을 때까지 반복
    if (count == 0): # count == 0 이라면 카드를 뽑아서 버릴 순서
        k = cards.popleft()
        result.append(k)
        count+=1
    elif (count == 1): # count == 1 이라면 카드를 뽑아서 카드 아래로 내릴 순선
        k = cards.popleft()
        cards.append(k)
        count = 0
result.append(cards[0]) # 마지막 남은 result 에 저장
for i in result:
    print(i, end = " ")
