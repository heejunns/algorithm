# 프로그래머스 진료 순서 정하기 (level 0)
def solution(emergency):
    answer = []
    x = sorted(emergency)
    x.reverse()
    for i in range(len(emergency)):
        answer.append(x.index(emergency[i])+1)
    return answer
