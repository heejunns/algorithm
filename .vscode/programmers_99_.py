# 프로그래머스 평균 구하기 (level 1)
def solution(arr):
    answer = 0
    total = 0
    for i in arr:
        total+=i
    answer = total/len(arr)
    return answer