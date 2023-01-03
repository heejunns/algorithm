# 프로그래머스 두 정수 사이의 합 (level 1)
def solution(a, b):
    answer = 0
    x = [a,b]
    x.sort() # range를 사용해 값을 더해주기 위해서 오름차순으로 정렬 해주기
    for i in range(x[0],x[1]+1):
        answer+=i
    return answer
