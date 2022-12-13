# 프로그래머스 최댓값 만들기(1) (level 0)
def solution(numbers):
    x = max(numbers)
    numbers.pop(numbers.index(x))
    y = max(numbers)
    answer = x*y
    return answer
