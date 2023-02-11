# 프로그래머스 세균 증식 (level 0)
def solution(n, t):
    answer = n
    for i in range(t):
        answer*=2
    return answer