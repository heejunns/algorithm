# 프로그래머스 개미 군단 (level 0)
def solution(hp):
    answer = 0
    x = [5,3,1]
    for i in x:
        answer += hp//i
        hp%=i
    return answer