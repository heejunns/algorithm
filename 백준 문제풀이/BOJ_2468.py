# 백준 2468번, 안전 영역
import copy 
import sys
from collections import deque


# 위 아래 좌 우 방향 리스트
dx= [0,1,0,-1] 
dy = [1,0,-1,0] 

n = int(sys.stdin.readline()) # 2차원 배열의 행과 열의 개수를 나타내는 n 입력받기

info = [] # 높이 정보를 저장할 리스트

max_height = 0 # 압력받은 높이 중 가장 높은 위치를 저장할 변수

for i in range(n): # 높이 정보 입력받기
    input_area = list(map(int,sys.stdin.readline().rstrip().split()))
    info.append(input_area)
    if max_height < max(input_area): # 입력받은 높이 중 가장 높은 높이 찾기
        max_height = max(input_area) # 가장 높은 높이로 저장


def dfs(a,b,current_height, subinfo):
    queue = deque([])
    queue.append([a,b])

    while queue:
        pop_element = queue.popleft()
        for i in range(4):
            x = pop_element[0] + dx[i]
            y = pop_element[1] + dy[i]
            if (x >=0 and x<n )and (y >=0  and y <n):
                if subinfo[x][y] > current_height: # 현재 물에 잠기는 높이보다 크다면
                    subinfo[x][y] = current_height # 다시 방문하지 못하도록 현재 물의 높이를 저장
                    queue.append([x,y]) # 안전영역의 위치를 저장

result = []
for i in range(max_height):
    count = 0 # dfs 함수가 호출되는 개수를 셀 변수, 이 개수가 안전영역의 개수가 된다.
    subinfo = copy.deepcopy(info) # 0 부터 입력받은 높이 -1 까지의 모든 경우의 수로 안전한 영역을 찾아야 하기 때문에 높이 정보 를 복사해서 쓰기
    for l in range(n):
        for k in range(n):
            if subinfo[l][k] > i: # 현재 경우의 수 값보다 크다면
                count+=1
                dfs(l,k,i,subinfo)

    result.append(count) # 각 경우의 수마다 안전영역의 개수 count 를 저장

if max(result) == 0 : # 모든 경우에서 안전영역의 최대가 0 개라면 물에 잠기지 않는 경우이기 때문에 1
    print(1)
else:
    print(max(result)) # 모든 경우의 수에서 가장 많은 안전영역의 수를 출력




    


