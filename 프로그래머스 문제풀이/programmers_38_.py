# 프로그래머스 자릿수 더하기 (level 0)
def solution(n):
    answer = 0 
    s = str(n)
    for i in s:
        answer+= int(i)
    return answer