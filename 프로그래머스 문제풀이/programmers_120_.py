# 프로그래머스 나누어 떨어지는 숫자 배열 (level 1)
def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer