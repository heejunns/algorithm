# 프로그래머스 아이스 아메리카노 (level 0)
def solution(money):
    answer = []
    x = money//5500
    answer.append(x)
    answer.append(money%5500)
    return answer
    
