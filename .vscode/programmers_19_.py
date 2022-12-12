# 프로그래머스 점의 위치 구하기 (level 0)
def solution(dot):
    answer = 0 
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0 :
        answer = 2
    elif dot[0] < 0 and dot[1] < 0 :
        answer = 3
    elif dot[0] > 0 and dot[1] < 0 :
        answer = 4
    return answer
