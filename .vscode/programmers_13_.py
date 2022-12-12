# 프로그래머스 양꼬리 (level 0)
def solution(n, k): 
    x = n//10
    y = k-x
    answer = (12000*n)+(y*2000)
    return answer
   
print(solution(10,1))