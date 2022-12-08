# 프로그래머스 게임 맵 최단거리
# 최단거리 해결 문제니까 BFS 너비 우선 탐색으로 풀기
from collections import deque
def solution(maps):
    visited = [[False for i in range(len(maps[0]))] for i in range(len(maps))]
    queue = deque()
    index1 = 0
    index2 = 0
    answer = 1
    queue.append([index1,index2,answer])
    visited[0][0] = True
    while queue:
        index1,index2,answer = queue.popleft() 
        if index1 == len(maps)-1 and index2 == len(maps[0])-1:
            break
        answer+=1
        if index2+1 < len(maps[0]): # x좌표 + 움직임
            if maps[index1][index2+1] == 1:
                if visited[index1][index2+1] == False:
                    visited[index1][index2+1] = True # 미 방문시 방문처리
                    queue.append([index1,index2+1,answer]) 
        if index2-1 >= 0 : # x 좌표 - 움직임 
            if maps[index1][index2-1] == 1 :
                if visited[index1][index2-1] == False:
                    visited[index1][index2-1] =  True # 미 방문시 방문처리
                    queue.append([index1,index2-1,answer])
        if index1+1 < len(maps) : # y 좌표 + 움직임
            if maps[index1+1][index2]==1:
                if visited[index1+1][index2] == False:
                    visited[index1+1][index2] = True # 미 방문시 방문처리
                    queue.append([index1+1,index2,answer])
        if index1-1 >= 0 : # y좌표 - 움직임
            if maps[index1-1][index2] == 1:
                if visited[index1-1][index2] == False:
                    visited[index1-1][index2] = True # 미 방문시 방문처리
                    queue.append([index1-1,index2,answer])
    if  index1 != len(maps)-1 or index2 != len(maps[0])-1:
        answer = -1
    return answer
