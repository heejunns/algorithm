# 프로그래머스 특정 문자 제거하기 (level 0)
def solution(my_string, letter):
    answer = ""
    for i in my_string:
        if i != letter:
            answer+=i
    return answer