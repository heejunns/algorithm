# 백준 10773번, 제로
import sys
n = int(sys.stdin.readline()) # 정수의 개수 입력 받기
total = [] # 입력 받은 정수를 저장할 리스트
for i in range(n):
    inputs = int(sys.stdin.readline())
    if(inputs == 0): # 입력 받은 정수가 0 이라면
        total.pop() # total 리스트에서 하나 꺼내기
    else:
        total.append(inputs) # 입력 받은 정수가 0 이 아니라면 total 리스트에 추가
print(sum(total))