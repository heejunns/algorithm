# 프로그래머스 삼각형의 완성조건 (1)
def solution(sides):
    answer = 1
    x = max(sides)
    sides.pop(sides.index(x))
    if x >= sum(sides):
        answer = 2
    return answer
    