# 프로그래머스 옷가게 할인 받기 (level 0)
def solution(price):
    answer = price
    if price >= 500000:
        answer = price*0.8
    elif price >= 300000:
        answer = price*0.9
    elif price >= 100000:
        answer = price*0.95
    return int(answer)