# 프로그래머스 짝수는 싫어요 (level 0)
def solution(n):
    answer = []
    for i in range(1,n+1):
        if i%2 != 0:
            answer.append(i)
    return answer
print(solution(10))