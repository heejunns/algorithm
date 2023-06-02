# 백준 7576번, 토마토
import sys
from collections import deque
# 위 아래 좌 우 방향 리스트
dx= [0,1,0,-1] 
dy = [1,0,-1,0]

# dfs 방법의 함수 만들기
def dfs(queue):
    tomatoDay = [] # 토마토가 모두 
    while queue :
        pop_element = queue.popleft()
        for i in range(4):
            x = pop_element[0]+dx[i]
            y = pop_element[1]+dy[i]
            if (x >=0 and x<n )and (y >=0  and y <m): # 범위에서 벗어나지 않는다면
                if info[x][y] == 0: # 익은 토마토라면
                    info[x][y] = info[pop_element[0]][pop_element[1]]+1 # 해당 queue 에서 꺼낸 토마토의 위치의 info 값에서 +1
                    tomatoDay.append(info[pop_element[0]][pop_element[1]]+1) # 익힌 토마토의 info 에 저장할 값을 저장, 이 값이 토마토를 익히는데 걸린 날짜이다.
                    queue.append([x,y]) # 익힌 토마토의 위치 정보를 queue 에 저장
    return tomatoDay

m,n = map(int,sys.stdin.readline().rstrip().split()) # 상자의 크기를 나타내는 m, n 입력받기, m 은 상자의 가로 칸의 수 , n 은 상자의 세로 칸의 수


info = [] # 상자에 담긴 익힌 토마토의 정보를 기록할 리스트

for i in range(n):
    input_tomato = list(map(int,sys.stdin.readline().rstrip().split())) # 상자 가로줄에 들어있는 토마토의 정보를 n 개 입력받기
    info.append(input_tomato) 

queue = deque([]) # 익힌 토마토가 들어있는 칸의 정보를 담을 queue

# 입력받은 상자의 정보를 모두 확인해서 익힌 토마토가 있는 칸의 정보를 queue 에 저장
for i in range(n):
    for l in range(m):
        if info[i][l] == 1:
            queue.append([i,l])

# 토마토에 의해서 익지 않은 토마토를 dfs 방법에 의해서 모두 익힌 날짜 정보를 리턴 받기
result = dfs(queue) 

why_tomato = False # 아직 익지 않는 토마토가 있는지 여부를 저장할 변수
for i in range(n): # 익지 않은 토마토가 있는지 확인
    for l in range(m):
        if info[i][l] ==  0:
            why_tomato = True
if why_tomato == True: # why_tomato 의 값이 true 라면 익지 않은 토마토가 있다는 뜻이니까 
    print(-1)
elif len(result) == 0: # dfs 함수를 호출하고 반환받은 값에 아무 값도 없다면 처음부터 토마토는 모두 익어 있었다는 뜻이니까
    print(0)
else:
    print(result[-1]-1) # 토마토를 모두 익힌 날짜의 정보에서 가장 마지막에 들어온 날짜가 모든 토마토를 익힌 날짜니까 여기서 -1 을 한다. -1 을 하는 이유는 처음 익어있던 토마토에 정보인 1 은 빼야하기 때문이다.




