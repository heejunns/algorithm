# 이코테 2021 강의 BFS 예제코드
from collections import deque
node = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],[1, 7]]
visited = [False]* 9

def bfs(node, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        i = queue.popleft()
        print(i, end = " ")

        for l in node[i]:
            if visited[l] == False:
                queue.append(l)
                visited[l] = True

bfs(node,1,visited)


