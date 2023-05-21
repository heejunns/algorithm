# 백준 2178번, 미로탐색
import sys
from collections import deque
# 상하좌우
dx = [0,0,1,-1] 
dy = [1,-1,0,0]

n,m = map(int, sys.stdin.readline().rstrip().split()) # n,m 입력받기
info = [] # 미로의 정보를 저장할 리스트
for i in range(n): # 미로의 정보 입력받기
    input_data = list(map(int,sys.stdin.readline().rstrip()))
    info.append(input_data)

def dfs(info,a,b):
    queue = deque([])
    queue.append([a,b]) 
    while queue : 
        pop_element = queue.popleft()
        for i in range(4):
            x = pop_element[0]+ dx[i]
            y = pop_element[1]+ dy[i]
            if x < 0 or x>=n or y < 0  or y >= m:
                continue
            if info[x][y] == 1: # 해당 칸이 1 이라면
                info[x][y] = info[pop_element[0]][pop_element[1]] +1 # 현재 뽑은 칸의 숫자보다 +1 로 저장
                queue.append([x,y]) 
        if info[n-1][m-1] > 1: # 오른쪽 제일 아래 칸이 1 보다 크다는건 어떤 방향으로든 가장 빨리 최단 경로로 도착 했다는 뜻 이니까 종료
            break
        info[pop_element[0]][pop_element[1]] = 0 # 방문한 칸은 0 으로 만들기
    return info[n-1][m-1] # 오른쪽 제일 아래 칸에 저장 되어 있는 숫자 반환
print(dfs(info,0,0))
