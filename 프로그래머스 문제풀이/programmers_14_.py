# 프로그래머스 중복된 숫자 개수 (level 0)
def solution(array, n):
    answer = array.count(n)
    return answer
print(solution([1,2,3,3,3,3,3,3,3,3,],3))