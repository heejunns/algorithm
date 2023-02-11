# 프로그래머스 최댓값 만들기 (2) (level 0)
def solution(numbers):
    numbers.sort()
    answer = numbers[-2]*numbers[-1]
    if (numbers[0]*numbers[1])> (numbers[-2]*numbers[-1]):
        answer = numbers[0]*numbers[1]
    return answer