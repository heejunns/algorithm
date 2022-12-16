# 프로그래머스 가장 큰 수 찾기 (level 0)
def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer