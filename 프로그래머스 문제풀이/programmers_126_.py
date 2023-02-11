# 프로그래머스 콜라츠 추측 (level 1)
def solution(num):
    answer = 0 # num이 1이라면 아래 if 문이 false니까 0 이 그대로 출력
    if num != 1:
        while answer <=500:
            if num == 1: # 1이 된다면 탈출
                break
            if num%2 == 0: # num이 짝수라면
                num = (num//2)
                answer+=1
            elif num%2 == 1: # 홀수라면
                num = ((num*3)+1)
                answer+=1
    if answer > 500: # 작업이 500번이 넘으면
        answer = -1
    return answer