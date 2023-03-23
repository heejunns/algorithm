# 백준 1021 번, 회전하는 큐
import sys
from  collections import deque
n,m = map(int, sys.stdin.readline().rstrip().split()) # 큐의 크기 n, 뽑아내려는 숫자의 개수 m 을 입력받기
queue_list = deque([i for i in range(1,n+1)]) # n 만큼 숫자 넣기, 0 번 인덱스부터 1~n+1 까지 숫자 채우기
count = 0 # 2, 3번 연산을 할 때 연산 횟수를 세기위한 변수
input_list = list(map(int, sys.stdin.readline().rstrip().split())) # 뽑으려는 수의 위치 입력받기
for l in input_list:
        if queue_list.index(l) == 0: # 뽑으려는 수의 위치가 0 번 자리에 있다면
            queue_list.popleft()
        else:
            if (len(queue_list) - queue_list.index(l)) < queue_list.index(l): # 3번 연산
                for i in range(len(queue_list) - queue_list.index(l)):
                    count+=1
                    a = queue_list.pop()
                    queue_list.appendleft(a)
                queue_list.popleft()
            else: # 2번 연산
                for i in range(queue_list.index(l)):
                    count+=1
                    b = queue_list.popleft()
                    queue_list.append(b)
                queue_list.popleft()
print(count)