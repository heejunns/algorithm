# 백준 1021 번, 회전하는 큐
import sys
from  collections import deque
n,m = map(int, sys.stdin.readline().rstrip().split())
queue_list = deque([i for i in range(1,n+1)])
count = 0
input_list = list(map(int, sys.stdin.readline().rstrip().split()))
for l in input_list:
        if queue_list.index(l) == 0:
            queue_list.popleft()
        else:
            if (len(queue_list) - queue_list.index(l)) < queue_list.index(l):
                for i in range(len(queue_list) - queue_list.index(l)):
                    count+=1
                    a = queue_list.pop()
                    queue_list.appendleft(a)
                queue_list.popleft()
            else:
                for i in range(queue_list.index(l)):
                    count+=1
                    b = queue_list.popleft()
                    queue_list.append(b)
                queue_list.popleft()
print(count)