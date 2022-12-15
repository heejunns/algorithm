# 프로그래머스 숫자 찾기 (level 0)
def solution(num, k):
    answer = 0
    if str(k) not in str(num):
        answer = -1
    else:
        for i in str(num):
            if i == str(k):
                answer +=1
                break
            answer+=1
    return answer