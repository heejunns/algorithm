# 이코테 bfs 연습문제 미로 탈출 
from collections import deque
n,m = map(int,input().split()) # n x m 입력 받기 
graph = []
for i in range(n): # 맵의 정보를 입력 받기 
    graph.append(list(map(int,input())))
# 상하좌우를 움직여서 범위에 넘어가는지 확인하기 위해 사용 
nx = [-1, 1, 0 , 0] 
ny = [0, 0, -1, 1]
def miro(x,y):
    queue = deque([x,y]) # 입력되는 위치를 리스트 형태로 deque에 추가 
    while queue:
        x = queue.popleft() # x 위치 꺼내기
        y = queue.popleft() # y 위치 꺼내기

        for i in range(4): # 상하좌우를 확인하기 위해 0~3 인덱스를 확인 
            dx = nx[i] + x 
            dy = ny[i] + y
            if dx < 0 or dx >= n or dy < 0 or dy >= m: # 범위에 벗어나면 해당하지 않기 때문에 무시하고 continue로 다른 방향으로 이동
                continue
            if graph[dx][dy] == 0: # 범위에 벗어나지 않더라도 그 자리가 0이면 갈수 없기 때문에 무시하고 continue로 다른 방향으로 이동
                continue
            if graph[dx][dy] == 1: 
                graph[dx][dy] = graph[x][y] + 1 # 이동했을때 범위가 1이면 이동 가능하기 때문에 움직인 거리를 기록, 꺼낸 위치에 기록된 이동거리에 +1을 해서 기록
                queue.extend([dx,dy]) # 이동 가능한 위치 deque에 추가 
    return graph[n-1][m-1] # 맨 오른쪽 아래에 기록된 이동거리
print(miro(0,0)) 