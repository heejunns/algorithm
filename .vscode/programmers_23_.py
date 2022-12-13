# 프로그래머스 피자 나눠 먹기 (3) (level 0)
def solution(slice, n):
    if n%slice == 0:
        answer = n//slice
    elif n%slice > 0 :
        answer = (n//slice)+1
    return answer
    