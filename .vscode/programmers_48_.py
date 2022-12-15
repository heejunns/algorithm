# 프로그래머스 7의 개수 (level 0)
def solution(array):
    answer = 0
    for i in array:
        for l in str(i):
            if str(l) == "7":
                answer+=1
    return answer