# 프로그래머스 중복된 문자 제거 (level 0)
def solution(my_string):
    answer = ""
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer