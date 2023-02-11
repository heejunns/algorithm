# 프로그래머스 문자열안에 문자열 (level 0)
def solution(str1, str2):
    answer = 2
    if str2 in str1:
        answer = 1
    return answer