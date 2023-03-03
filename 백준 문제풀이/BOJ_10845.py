# 백준 10845번, 큐
import sys
from collections import deque
n = int(sys.stdin.readline())
total_queue = deque([])
result = []
for i in range(n):
    inputs = list(map(str,sys.stdin.readline().rstrip().split()))
    if (inputs[0] == "push"):
        total_queue.append(inputs[1])
    elif (inputs[0] == "pop"):
        if len(total_queue) == 0:
            result.append(-1)
        else:
            result.append(total_queue.popleft())
    elif (inputs[0] == "size"):
        result.append(len(total_queue))
    elif (inputs[0]== "empty"):
        if len(total_queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif (inputs[0]== "front"):
        if len(total_queue) == 0:
            result.append(-1)
        else:
            result.append(total_queue[0])
    elif (inputs[0] == "back"):
        if len(total_queue) == 0:
            result.append(-1)
        else:
            result.append(total_queue[-1])
for i in result:
    print(i)