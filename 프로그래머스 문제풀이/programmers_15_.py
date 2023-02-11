# 프로그래머스 머쓱이보다 키 큰 사람 (level 0)
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer+=1
    return answer
print(solution([1,2,3],1))