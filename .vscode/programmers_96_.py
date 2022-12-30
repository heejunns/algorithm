# 프로그래머스 나머지가 1이 되는 수 찾기 (level 1)
def solution(n):
    answer = 0
    for i in range(1,n):
        if n%i == 1:
            answer = i
            break
    return answer