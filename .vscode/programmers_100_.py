# 프로그래머스 짝수와 홀수 (level 1)
def solution(num):
    answer = "Odd"
    if num%2 == 0:
        answer = "Even"
    
    return answer