# 프로그래머스 가운데 글자 가져오기 (level 1)
def solution(s):
    answer = ""
    if len(s)%2 == 0: # 문자열 s의 길이가 짝수일때
        answer+= s[(len(s)//2)-1:(len(s)//2)+1]
    else: # 문자열 s의 길이가 홀수일때
        answer+= s[len(s)//2]
    return answer