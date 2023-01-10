# 프로그래머스 최솟값 만들기 (level 2)
def solution(A,B): # 하나의 리스트에서는 가장 작은 값을 또 하나의 나머지 리스트에서는 최대 값을 뽑아 곱하고 더하는 솔루션
    answer = 0
    A.sort() # 오름차순으로 정렬 
    B.sort(reverse=True) # 내림차순으로 정렬
    for i in range(len(A)): # 하나씩 꺼내기
        x = A[i] 
        y = B[i]
        answer+= (x*y) # 곱하고 그 값을 더하기
    return answer 