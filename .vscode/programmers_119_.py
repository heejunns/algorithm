# 프로그래머스 정수 제곱근 판별 (level 1)
def solution(n):
    answer = 0
    m = 1
    while m <= n:
        if m*m == n:
            answer = (m+1)*(m+1)
            break
        m+=1
    if answer == 0:
        answer = -1
    return answer