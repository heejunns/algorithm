# 프로그래머스 x만큼 간격이 있는 n개의 숫자 (level 1)
def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer