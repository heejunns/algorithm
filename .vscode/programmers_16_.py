# 프로그래머스 피자 나눠 먹기(1) (level 0)
def solution(n):
    if n%7 == 0:
        answer = n//7
    else:
        answer = (n//7)+1
    return answer