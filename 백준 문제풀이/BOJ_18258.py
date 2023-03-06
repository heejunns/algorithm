# 백준 18258번, 큐 2
import sys
from collections import deque
n = int(sys.stdin.readline()) # 명령의 수 n 입력받기
queue_list = deque([])
result = []
for i in range(n):
    inputs = list(map(str,sys.stdin.readline().rstrip().split())) # 명령 한개씩 입력받기
    if (inputs[0] == "push"):
        queue_list.append(inputs[1])
    elif (inputs[0] == "pop"):
        if(len(queue_list) == 0):
            result.append(-1)
        else:
            result.append(queue_list.popleft())
    elif (inputs[0] == "size"):
        result.append(len(queue_list))
    elif (inputs[0] == "empty"):
        if(len(queue_list) == 0):
            result.append(1)
        else:
            result.append(0)
    elif (inputs[0] == "front"):
        if(len(queue_list) == 0):
            result.append(-1)
        else:
            result.append(queue_list[0])
    elif (inputs[0] == "back"):
        if(len(queue_list) == 0):
            result.append(-1)
        else:
            result.append(queue_list[-1])
for j in result:
    print(j)


