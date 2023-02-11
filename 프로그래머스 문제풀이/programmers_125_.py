# 프로그래머스 3진법 뒤집기 (level 1)
def solution(n):
    answer = 0
    x = []
    while True:
        if n < 3:
            answer = n
            break
        if n//3 < 3:
            x.insert(0,n%3)
            x.insert(0,n//3)
            break
        x.insert(0,n%3)
        n = (n//3)
    if x != []:
        for i in range(len(x)):
            answer+= ((3**i)*x[i])
    return answer