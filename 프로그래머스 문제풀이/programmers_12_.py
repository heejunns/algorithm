# 프로그래머스, 짝수의 합 (level 0)
def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2 == 0:
            answer+=i
    return answer