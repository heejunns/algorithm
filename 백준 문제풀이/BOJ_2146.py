# 백준 2146 번 , 카드 2, total 의 가장 왼쪽이 위에 있는 카드로 기준을 정한다.
import sys
from collections import deque
n = int(sys.stdin.readline()) # 정수 n 입력 받기
total = deque([i for i in range(1,n+1)]) # 1 부터 입력 받은 정수 n 까지 수를 리스트로 만들기
check = 0 # 카드를 꺼내서 버릴지 꺼내서 아래로 내릴지 판단하기 위한 변수
while len(total) > 1: # total 의 요소가 하나 남을때까지 반복
    if check == 0: # check 의 값이 0 이라면
        total.popleft() # 왼쪽 total 요소 꺼내서 버리기
        check+=1 
    elif check == 1: # check 의 값이 1 이라면
        m = total.popleft() # total 의 왼쪽 요소 꺼내서 다시 오른쪽으로 추가하기
        total.append(m)
        check = 0  # check 값 0 으로 변경
print(total[0])