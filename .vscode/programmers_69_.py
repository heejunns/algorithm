# 프로그래머스 팩토리얼 (level 0)
def solution(n):
    answer = 1
    k = 1
    while True:
        if k == n:
            break
        elif k>n:
            answer-=1
            break
        answer+=1
        k*=answer
    return answer
