# 프로그래머스 제곱수 판별하기 (level 0)
def solution(n):
    answer = 2
    for i in range(1,10000001):
        if i*i == n:
            answer = 1
            break
    return answer