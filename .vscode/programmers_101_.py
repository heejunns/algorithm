# 프로그래머스 정수 내림차순으로 배치하기 (level 1)
def solution(n):
    answer = 0
    x = []
    for i in str(n):
        x.append(i)
    x.sort()
    x.reverse()
    answer = "".join(x)
    return int(answer)