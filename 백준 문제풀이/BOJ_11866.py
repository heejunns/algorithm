# 백준 11866번, 요세푸스 문제 0
import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split()) # n, k 입력 받기
answer = [i for i in range(1,n+1)] # 1 부터 n 까지 리스트 만들기
result = [] # 제거한 요소들을 저장한 리스트
count = k # k 번째 요소를 제거하기 위해서 count 에 k 를 저장 
x = deque(answer)
while len(x) > 1:
    count-=1
    if count == 0:  
        result.append(x.popleft())
        count = k # k 번째 요소를 제거하기 위해서 count 에 k 를 다시 저장 
    else:
        m = x.popleft() # 앞의 요소를 꺼내서 
        x.append(m) # 다시 뒤에 저장
result.append(x[0]) # 마지막 남은 요소 result 리스트에 저장

print("<", end = "")
for i in range(len(result)-1):
        print(str(result[i])+", ",end = "")
print(result[-1], end = "")
print(">")
