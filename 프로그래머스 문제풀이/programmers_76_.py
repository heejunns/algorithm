# 프로그래머스 공 던지기 (level 0)
def solution(numbers, k):
    n = k-1
    i = (2*n)%(len(numbers))
    return numbers[i]
