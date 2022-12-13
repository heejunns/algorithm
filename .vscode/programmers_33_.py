# 프로그래머스 중앙값 구하기 (level 0)
def solution(array):
    array.sort()
    x = len(array)//2 
    answer = array[x]
    return answer

