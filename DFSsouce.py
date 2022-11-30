# 파이썬 이코테 DFS 예제 코드 연습, 재귀 함수로 구현 
node = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] # 각각 연결된 노드의 정보 
visited = [False] * 9 # 방문 정보를 표현 
def Dfs(node,inp, visited):
       visited[inp] = True
       print(inp, end=" ")
       for i in node[inp]:
              if visited[i] != True:
                Dfs(node,i,visited)                     

print(Dfs(node,1,visited))