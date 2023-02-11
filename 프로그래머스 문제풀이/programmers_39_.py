# 프로그래머스 모음 제거 (level 0)
def solution(my_string):
    x = ["a","e","i","o","u"]
    answer = ''
    for i in my_string:
        if i not in x:
            answer+=i
    return answer