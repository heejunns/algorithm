# 프로그래머스 문자열 밀기 (level 0)
def solution(A, B):
    answer = 0
    str = ""
    if A != B:
        for i in range(len(A)):
            A = A[len(A)-1] + A[0:len(A)-1]
            answer+=1
            if A == B:
                break
        if A != B:
            answer = -1
    return answer