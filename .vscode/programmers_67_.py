# 프로그래머스 합성수 찾기 (level 0)
def solution(n):
    answer = 0
    for i in range(4,n+1):
        for l in range(2,i):
            if i%l == 0:
                answer+=1
                break
    return answer