# 프로그래머스 부족한 금액 계산하기 (level 1)
def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1,count+1): # 이용 금액 확인하기
        total+=(price*i) 

    if money-total >=0: # 가지고 있는 돈으로 이용 금액을 지불했을때 돈이 남거나 딱 맞는다면
        answer = 0
    else:
        answer = total - money # 부족하다면 얼마나 부족한지 
    return answer