# 프로그래머스 가까운 수 (level 0)
def solution(array, n):
    answer = 0
    array.sort()
    x = []
    for i in array:
        x.append(abs(i-n))
    answer = array[x.index(min(x))]
    return answer