# 프로그래머스 콜라 문제 (level 1)
def solution(a, b, n):
    answer = 0
    while True:
        if n >= a: # 가지고 있는 빈병 n개가 돌려줘서 콜라를 받을 수 있는 빈병 a개보다 같거나 크면
            answer += ((n//a)*b) # 돌려받는 콜라 개수 
            n = ((n%a) + ((n//a)*b)) # 현재 남은 콜라 개수 (콜라로 바꾸지 못한 병의 개수 + 콜라병을 주고 콜라로 받은 개수)
        else: # 가지고 있는 빈병 n개가 돌려줘서 콜라를 받을 수 있는 빈병 a개보다 작으면
            break 
    return answer