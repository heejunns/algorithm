# 프로그래머스 두 개 뽑아서 더하기 (level 1)
def solution(numbers):
    answer = []
    n = 0 # 시작 인덱스
    while n< len(numbers): # 입력되는 numbers 리스트의 끝 인덱스보다 커지면 while문 종료
        for i in numbers[n:]: # 첫번째 인덱스 값과 나머지 인덱스 값들을 하나씩 더하기 
            for l in numbers[n+1:]: 
                if i+l not in answer: # 중복되는 값 제거하기 위한 if 문
                    answer.append(i+l)
            n+=1
    answer.sort() # 오름차순 정리
    return answer