# 프로그래머스 피자 나눠 먹기 (2) (level 0)
def solution(n):
    x = 6
    answer = 1
    while (True):
        if (x*answer)%n == 0:
            break
        answer+=1
    return answer