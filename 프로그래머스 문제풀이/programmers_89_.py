# 프로그래머스 직사각형 넓이 구하기 (level 0)
def solution(dots):
    answer = 0
    x = dots[0][0]
    y = dots[0][1]
    for i in dots[1:]:
        if x != i[0] and y != i[1]:
            x = abs(x-i[0])
            y = abs(y-i[1])
            break
    return x*y