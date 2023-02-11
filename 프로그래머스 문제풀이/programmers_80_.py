# 프로그래머스 외계어 사전 (level 0)
def solution(spell, dic):
    answer = 2
    x = 0
    for i in dic:
        for l in spell:
            if l in i:
                x+=1
        if x >= len(spell):
            answer = 1
            break
        else:
            x = 0
    return answer
