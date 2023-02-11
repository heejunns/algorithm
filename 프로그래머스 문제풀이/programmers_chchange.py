# 프로그래머스 단어 변환 DFS, BFS
# BFS 를 사용해서 해결
# 꺼내는 문자열과 문자 하나만 다른 문자열을 words 리스트에서 어떻게 찾아 낼 것인가?
# 나의 아이디어는 2중 for문을 통해서 words의 원소를 하나씩 꺼내서 begin과 비교해 하나의 문자만 다를때 그 문자를 queue에 넣는 방식의 아이디어다.
from collections import deque 
def solution(begin, target, words):
    answer = 0
    if not(target in words):
        answer = 0
    else:
        visited = [False for i in range(len(words))]
        queue = deque()
        queue.append([begin,answer])
        while queue:
            x,answer = queue.popleft()
            if x == target:
                break
            answer+=1
            for i in words:
                m = 0
                if visited[words.index(i)] == False:
                    for l in range(len(begin)):
                        if i[l] != x[l]:
                            m+=1
                    if m == 1 :
                        visited[words.index(i)] = True
                        queue.append([i,answer])
    return answer
