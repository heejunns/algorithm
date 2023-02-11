# 프로그래머스 배열 회전시키기 (level 0)
def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        answer.extend(numbers[:len(numbers)-1])
    elif direction == "left":
        answer.extend(numbers[1:])
        answer.append(numbers[0])
    return answer