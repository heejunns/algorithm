# 프로그래머스 치킨 쿠폰 (level 0)
def solution(chicken): # 치킨의 개수와 쿠폰의 개수를 같다. 
    answer = 0
    while chicken >= 10: # 쿠폰이 10개가 되지 못하면 사용불가니까 탈출
        answer += (chicken//10) # 시킨 치킨 10마리당 10개의 쿠폰으로 다시 한마리의 치킨을 시킬수 있으니까 쿠폰 10개로 나눠 서비스 치킨을 계산
        chicken = (chicken%10) + (chicken//10) # 쿠폰으로 서비스 치킨을 받을 수 있는 쿠폰 10씩을 모두 사용하고 사용하지 못한 쿠폰 + 쿠폰으로 시킨 치킨을 시키면 받는 쿠폰
    return answer