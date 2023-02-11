# 프로그래머스 DFS, BFS 네트워크
# DFS로 풀기
def solution(n, computers):
    answer = 0
    visited = [False]*n
    def dfs(i):
        visited[i] = True
        for l in range(n):
            if computers[i][l] and not visited[l]:
                dfs(l)

    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer+=1

    return answer
