# 이코테 2021 강의 DFS,BFS 연습문제
import sys
sys.setrecursionlimit(10**5)
n,m = map(int,input().split()) # 세로의 길이 n, 가로의 길이 m 
node  = []
def dfsexercise(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: # 범위를 넘어서는지 
        return False
    
    if node[x][y] == 0: # 0이라면 구멍이 뚫려 있으니까

        node[x][y] == 1 # 물을 넣었다고 기록 

        # 주변에 연결되서 구멍이 뚫려있는지 확인 
        dfsexercise(x-1,y) 
        dfsexercise(x+1,y)
        dfsexercise(x,y-1)
        dfsexercise(x,y+1)
        return True
    return False

for i in range(n):
    node.append(list(map(int,input())))

result = 0
for i in range(n):
    for l in range(m):
        if dfsexercise(i,l) == True:
            result += 1

print(result)