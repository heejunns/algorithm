# 프로그래머스 같은 숫자는 싫어 (level 1)
def solution(arr):
    answer = [arr[0]]
    x = arr[0]
    for i in arr[1:]:
        if x != i:
            answer.append(i)
            x = i
    return answer