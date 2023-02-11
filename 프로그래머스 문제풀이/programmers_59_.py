# 프로그래머스 암호 해독 (level 0)
def solution(cipher, code):
    answer = ''
    for i in range(1,len(cipher)+1):
        if i%(code) == 0:
            answer+=cipher[i-1]
    return answer