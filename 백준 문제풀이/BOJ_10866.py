# 백준 10866번, 덱
import sys
from collections import deque
n = int(sys.stdin.readline()) # 명령의 수 n 입력 받기
total = deque([]) # 덱 생성
result = [] # 출력 할 값을 저장 할 리스트
for i in range(n):
    inputs = list(map(str,sys.stdin.readline().rstrip().split())) # 각각의 명렬을 입력 받기
    if inputs[0] == "push_front":
        total.appendleft(int(inputs[1]))
    elif inputs[0] == "push_back":
        total.append(int(inputs[1]))
    elif inputs[0] == "pop_front":
        if len(total) == 0:
            result.append(-1)
        else:
            result.append(total.popleft())
    elif inputs[0] == "pop_back":
        if len(total) == 0:
            result.append(-1)
        else:
            result.append(total.pop())
    elif inputs[0] == "size":
        result.append(len(total))
    elif inputs[0] == "empty":
        if len(total) == 0:
            result.append(1)
        else:
            result.append(0)
    elif inputs[0] == "front":
        if len(total) == 0:
            result.append(-1)
        else:
            result.append(total[0])
    elif inputs[0] == "back":
        if len(total) == 0:
            result.append(-1)
        else:
            result.append(total[-1])
for i in result:
    print(i)
        
            

