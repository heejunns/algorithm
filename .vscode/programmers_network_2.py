# 프로그래머스 DFS, BFS 네트워크
# BFS로 풀기
from collections import deque
def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [False]*n

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            answer+=1
            queue.append(i)
        while queue:
            i = queue.popleft()
            for l in range(n):
                if computers[i][l] and not visited[l]:
                    visited[l] = True
                    queue.append(l)

    return answer
    

       

