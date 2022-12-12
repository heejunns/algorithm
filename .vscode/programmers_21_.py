# 프로그래머스 문자열 뒤집기 (level 0)
def solution(my_string):
    answer = ""
    x = len(my_string)
    while (x-1>=0):
        answer+= my_string[x-1]
        x-=1
    return answer
print(solution("ab"))
