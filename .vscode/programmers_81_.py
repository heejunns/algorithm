# 프로그래머스 컨트롤 제트 (level 0)
def solution(s):
    answer = 0
    x = s.split()
    while True:
        if "Z" in x:
            n = x.index("Z")
            m = n-1
            x.pop(n)
            x.pop(m)
        else:
            break
    for i in x:
        answer+= int(i)
    return answer