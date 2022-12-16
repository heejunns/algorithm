# 프로그래머스 한 번만 등장한 문자 (level 0)
def solution(s):
    x = []
    answer = []
    for i in s:
        if i not in x:
            x.append(i)
    for l in x:
        if s.count(l) == 1:
            answer.append(l)
    answer.sort()
    return "".join(answer)