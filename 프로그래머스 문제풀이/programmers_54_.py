# 프로그래머스 약수 구하기 (level 0) 
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i == 0:
            answer.append(i)
    return answer
