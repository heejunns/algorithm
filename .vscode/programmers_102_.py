# 프로그래머스 핸드폰 번호 가리기 (level 1)
def solution(phone_number):
    answer = ""
    x = (len(phone_number)-4)*"*"
    answer = x+phone_number[len(phone_number)-4:len(phone_number)]
    
    return answer