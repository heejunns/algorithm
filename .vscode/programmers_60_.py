# 프로그래머스 주사위의 개수 (level 0)
def solution(box, n):
    answer = box[0]//n
    for i in box[1:]:
        answer*= i//n
    return answer