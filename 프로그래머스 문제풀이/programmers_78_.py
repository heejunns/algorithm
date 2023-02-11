# 프로그래머스 과일 장수 (level 1)
def solution(k, m, score):
    answer = 0
    score.sort()
    score.reverse()
    x = []
    for i in score:
        x.append(i)
        if len(x) == m:
            answer+= (m*min(x))
            x = []
    return answer
