# 프로그래머스 구슬을 나누는 경우의 수 (level 0)
def solution(balls, share):
    x = 1
    y = 1
    z = 1
    for i in range(1,balls+1):
        x*=i
    for l in range(1,share+1):
        y*=l
    for k in range(1,(balls-share)+1):
        z*=k
    return x//(y*z)