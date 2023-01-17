# 프로그래머스 k의 개수 (level 0)
def solution(i, j, k):
    answer = 0
    for l in range(i,j+1):
         for s in str(l): # i 부터 j까지의 원소를 하나씩 꺼내고 그 각각의 원소를 숫자 한자리씩 꺼내어 k가 들어간다면 answer +1
                if str(k) == s:
                    answer+=1
    return answer