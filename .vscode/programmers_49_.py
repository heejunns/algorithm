# 프로그래머스 문자열 정렬하기 (2) (level 0)
def solution(my_string):
    x = my_string.lower()
    n = []
    for i in x:
        n.append(i)
    n.sort()
    return "".join(n)
print(solution("BASEqdwh"))