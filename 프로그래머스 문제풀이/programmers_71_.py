# 프로그래머스 A로 B 만들기 (level 0)
def solution(before, after):
    answer = 1
    for i in before:
        if before.count(i) != after.count(i):
            answer = 0
            break
    return answer