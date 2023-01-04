# 프로그래머스 약수의 개수와 덧셈 (level 1)
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        count = 0 
        for l in range(1,i+1):
            if i%l == 0: # 약수의 개수 기록하기
                count+=1
        if count%2 == 0: # 약수의 개수가 짝수면 더하기 
            answer+=i
        else: # 약수의 개수가 홀수면 빼기
            answer-=i
    return answer