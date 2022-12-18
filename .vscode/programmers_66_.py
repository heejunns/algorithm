# 프로그래머스 369게임 (level 0)
def solution(order):
    answer = 0
    for i in str(order):
        if int(i) == 3 or int(i)==6 or int(i)==9:
            answer+=1
    return answer